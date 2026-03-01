"""
Core game engine — all Monkopoly game logic, ported from Objects.py.
No UI dependencies. Returns events list for the WebSocket layer to relay.
"""
from __future__ import annotations

import random
from typing import Optional

from .ai import ai_property_buy_check, set_property_worth
from .constants import (
    BABOON_BIN_SPACES,
    BOARD_SIZE,
    BUS_SPACES,
    COLOR_SETS,
    COMPANY_SPACES,
    HEALTHCARE_HAZARD_SPACES,
    PURCHASABLE_SPACES,
    TAX_SPACES,
    TWO_PROPERTY_SETS,
)
from .models import GameState, create_initial_state


def new_game() -> GameState:
    state = create_initial_state()
    _update_all_worth(state)
    return state


def roll_dice(state: GameState) -> list[dict]:
    """Roll dice for the current player. Returns a list of event dicts."""
    events: list[dict] = []
    player = state.current_player()

    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    state.dice = [roll1, roll2]
    total = roll1 + roll2
    player.previous_roll = total

    if roll1 == roll2:
        state.doubles = True
        state.message = "DOUBLES!"
    else:
        state.doubles = False
        state.message = ""
        state.turn = (state.turn + 1) % len(state.players)

    events.append({
        "type": "dice_roll",
        "player": player.number,
        "dice": [roll1, roll2],
        "doubles": state.doubles,
    })

    old_position = player.board_position
    new_position = old_position + total
    passed_go = new_position >= BOARD_SIZE
    if passed_go:
        new_position -= BOARD_SIZE
        player.money += 200
        events.append({"type": "pass_go", "player": player.number, "money": player.money})

    player.board_position = new_position

    events.append({
        "type": "move",
        "player": player.number,
        "from": old_position,
        "to": new_position,
    })

    landing_events = _handle_landing(state, player.number)
    events.extend(landing_events)

    return events


def _handle_landing(state: GameState, player_num: int) -> list[dict]:
    """Handle what happens when a player lands on a space."""
    events: list[dict] = []
    player = state.players[player_num]
    space = state.board[player.board_position]

    if space.type == "go":
        player.money += 200
        state.message = "+$400"
        events.append({"type": "cash", "player": player_num, "amount": 200, "message": "+$400"})
        _advance_turn(state)

    elif space.type == "tax":
        tax_amount = TAX_SPACES[space.number]
        player.money -= tax_amount
        state.message = f"-${tax_amount}"
        events.append({"type": "cash", "player": player_num, "amount": -tax_amount, "message": f"-${tax_amount}"})
        _advance_turn(state)

    elif space.type == "gotojail":
        player.board_position = 10
        state.message = "GO TO BRAMPTON!"
        events.append({"type": "go_to_jail", "player": player_num})
        _advance_turn(state)

    elif space.type == "chest":
        card_index = random.randint(0, len(state._chest_cards) - 1)
        card = state._chest_cards[card_index]
        state.chest_card = card
        chest_type = "baboon_bin" if space.number in BABOON_BIN_SPACES else "healthcare_hazard"
        events.append({"type": "chest_card", "player": player_num, "card": card.to_dict(), "chestType": chest_type})

        if player.is_human:
            state.phase = "waiting_for_chest"
        else:
            events.extend(_execute_chest_card(state, player_num))

    elif space.number in PURCHASABLE_SPACES:
        if space.owner is None:
            if player.is_human:
                state.buy_property = space.number
                state.phase = "waiting_for_buy"
                events.append({"type": "buy_prompt", "player": player_num, "space": space.number})
            else:
                should_buy = ai_property_buy_check(player, space.number, state.board)
                if should_buy:
                    events.extend(_buy_property(state, player_num, space.number))
                else:
                    events.append({"type": "ai_pass", "player": player_num, "space": space.number})
                _advance_turn(state)
        else:
            if not space.mortgaged and space.owner != player_num:
                rent_events = _charge_rent(state, player_num, space)
                events.extend(rent_events)
            _advance_turn(state)

    else:
        _advance_turn(state)

    return events


def _advance_turn(state: GameState) -> None:
    """Set the phase for the next action depending on whose turn it is."""
    current = state.players[state.turn]
    if current.is_human:
        if state.doubles:
            state.phase = "waiting_for_roll"
        else:
            state.phase = "waiting_for_roll"
    else:
        state.phase = "ai_turn"


def acknowledge_chest(state: GameState) -> list[dict]:
    """Human player acknowledges a chest card."""
    events: list[dict] = []
    player = state.current_player()
    # The turn index was already advanced by roll_dice when doubles=False
    # We need the player who actually landed on the chest space
    # When doubles=True, turn hasn't advanced yet, so current_player is correct
    # When doubles=False, turn has advanced, so we need the previous player
    if state.doubles:
        landing_player_num = state.turn
    else:
        landing_player_num = (state.turn - 1) % len(state.players)

    events.extend(_execute_chest_card(state, landing_player_num))
    return events


def _execute_chest_card(state: GameState, player_num: int) -> list[dict]:
    """Execute the current chest card effect."""
    events: list[dict] = []
    card = state.chest_card
    if card is None:
        _advance_turn(state)
        return events

    player = state.players[player_num]
    player.money += card.money
    if card.money != 0:
        events.append({"type": "cash", "player": player_num, "amount": card.money,
                        "message": f"+${card.money}" if card.money > 0 else f"-${abs(card.money)}"})

    if card.move_to is not None:
        if card.move_to < player.board_position and card.move_to != 30:
            player.money += 200
            events.append({"type": "pass_go", "player": player_num, "money": player.money})

        old_pos = player.board_position
        player.board_position = card.move_to
        events.append({"type": "move", "player": player_num, "from": old_pos, "to": card.move_to})

        if card.move_to == 30:
            player.board_position = 10
            events.append({"type": "go_to_jail", "player": player_num})
            state.chest_card = None
            _advance_turn(state)
        else:
            state.chest_card = None
            landing_events = _handle_landing(state, player_num)
            events.extend(landing_events)
    else:
        state.chest_card = None
        _advance_turn(state)

    return events


def buy_property(state: GameState) -> list[dict]:
    """Human player buys the prompted property."""
    events: list[dict] = []
    space_num = state.buy_property
    if space_num is None:
        return events

    # Determine which player is buying (handle turn advancement from doubles logic)
    if state.doubles:
        buyer_num = state.turn
    else:
        buyer_num = (state.turn - 1) % len(state.players)

    events.extend(_buy_property(state, buyer_num, space_num))
    state.buy_property = None
    _advance_turn(state)
    return events


def pass_property(state: GameState) -> list[dict]:
    """Human player passes on buying."""
    state.buy_property = None
    _advance_turn(state)
    return [{"type": "pass_buy"}]


def _buy_property(state: GameState, player_num: int, space_num: int) -> list[dict]:
    """Execute a property purchase."""
    events: list[dict] = []
    player = state.players[player_num]
    space = state.board[space_num]

    space.owner = player_num
    player.money -= space.cost

    if space_num in COMPANY_SPACES:
        player.company_count += 1
    if space_num in BUS_SPACES:
        player.bus_count += 1

    _check_color_sets(state)
    _update_all_worth(state)

    events.append({
        "type": "property_bought",
        "player": player_num,
        "space": space_num,
        "cost": space.cost,
        "money": player.money,
    })
    return events


def _charge_rent(state: GameState, tenant_num: int, space) -> list[dict]:
    """Charge rent to the tenant from the property owner."""
    events: list[dict] = []
    tenant = state.players[tenant_num]
    owner = state.players[space.owner]

    if space.subtype == "company":
        both_owned = (state.board[12].owner == state.board[28].owner)
        rent = tenant.previous_roll * (10 if both_owned else 5)
    elif space.subtype == "bus":
        bus_count = sum(1 for s in state.board if s.subtype == "bus" and s.owner == space.owner)
        rent = int(12.5 * (2 ** bus_count))
    else:
        rent = space.rent[space.houses] if space.houses < len(space.rent) else 0

    tenant.money -= rent
    owner.money += rent

    events.append({
        "type": "rent_paid",
        "tenant": tenant_num,
        "owner": space.owner,
        "space": space.number,
        "rent": rent,
        "tenantMoney": tenant.money,
        "ownerMoney": owner.money,
    })
    return events


def _check_color_sets(state: GameState) -> None:
    """Update complete_set flags on all board spaces."""
    for set_num, spaces in COLOR_SETS.items():
        if set_num >= 9:
            continue
        owners = [state.board[s].owner for s in spaces]
        if all(o is not None and o == owners[0] for o in owners):
            for s in spaces:
                state.board[s].complete_set = True
        else:
            for s in spaces:
                state.board[s].complete_set = False


def _update_all_worth(state: GameState) -> None:
    for player in state.players:
        set_property_worth(player, state.board)


def mortgage_property(state: GameState, space_num: int) -> list[dict]:
    """Toggle mortgage on a property."""
    events: list[dict] = []
    space = state.board[space_num]
    if space.owner is None:
        return events

    player = state.players[space.owner]

    if not space.mortgaged:
        if space.houses > 0:
            return [{"type": "error", "message": "Cannot mortgage property with houses"}]
        space.mortgaged = True
        player.money += int(space.cost / 2)
        events.append({"type": "mortgage", "space": space_num, "player": space.owner, "money": player.money})
    else:
        unmortgage_cost = int(space.cost / 2 * 1.1)
        if player.money < unmortgage_cost:
            return [{"type": "error", "message": "Not enough money to unmortgage"}]
        space.mortgaged = False
        player.money -= unmortgage_cost
        events.append({"type": "unmortgage", "space": space_num, "player": space.owner, "money": player.money})

    return events


def add_house(state: GameState, space_num: int) -> list[dict]:
    """Add a house to a property."""
    space = state.board[space_num]
    if space.owner is None or space.subtype != "property":
        return [{"type": "error", "message": "Cannot add house here"}]

    player = state.players[space.owner]

    if space.houses >= 5:
        return [{"type": "error", "message": "Maximum houses reached"}]
    if space.mortgaged:
        return [{"type": "error", "message": "Cannot add house to mortgaged property"}]
    if not space.complete_set:
        return [{"type": "error", "message": "Need complete set to add houses"}]
    if player.money < space.house_cost:
        return [{"type": "error", "message": "Not enough money"}]

    # Even build rule: can't be more than 1 house ahead of others in set
    for s_num in COLOR_SETS.get(space.color_set, []):
        if space.houses == state.board[s_num].houses + 1:
            return [{"type": "error", "message": "Must build evenly across color set"}]

    space.houses += 1
    player.money -= space.house_cost

    return [{"type": "house_added", "space": space_num, "houses": space.houses,
             "player": space.owner, "money": player.money}]


def remove_house(state: GameState, space_num: int) -> list[dict]:
    """Remove a house from a property."""
    space = state.board[space_num]
    if space.owner is None or space.subtype != "property":
        return [{"type": "error", "message": "Cannot remove house here"}]

    if space.houses <= 0:
        return [{"type": "error", "message": "No houses to remove"}]
    if space.mortgaged:
        return [{"type": "error", "message": "Property is mortgaged"}]

    # Even build rule: can't be more than 1 house behind others in set
    for s_num in COLOR_SETS.get(space.color_set, []):
        if space.houses == state.board[s_num].houses - 1:
            return [{"type": "error", "message": "Must sell evenly across color set"}]

    player = state.players[space.owner]
    space.houses -= 1
    player.money += int(space.house_cost / 2)

    return [{"type": "house_removed", "space": space_num, "houses": space.houses,
             "player": space.owner, "money": player.money}]


def execute_trade(state: GameState, from_player: int, to_player: int,
                  from_properties: list[int], to_properties: list[int],
                  from_money: int, to_money: int) -> list[dict]:
    """Execute a trade between two players."""
    from .ai import ai_trade_check

    events: list[dict] = []

    # Validate no houses on traded properties
    for sp_num in from_properties + to_properties:
        if state.board[sp_num].houses > 0:
            return [{"type": "error", "message": "Cannot trade properties with houses"}]

    # AI trade check if trading with AI
    target = state.players[to_player]
    if not target.is_human:
        accepted = ai_trade_check(
            state, from_player, to_player,
            from_properties, to_properties,
            from_money, to_money,
        )
        if not accepted:
            return [{"type": "trade_denied"}]

    # Execute the trade
    p_from = state.players[from_player]
    p_to = state.players[to_player]

    p_from.money -= from_money
    p_from.money += to_money
    p_to.money -= to_money
    p_to.money += from_money

    for sp_num in from_properties:
        space = state.board[sp_num]
        if space.subtype == "company":
            p_from.company_count -= 1
            p_to.company_count += 1
        if space.subtype == "bus":
            p_from.bus_count -= 1
            p_to.bus_count += 1
        space.owner = to_player

    for sp_num in to_properties:
        space = state.board[sp_num]
        if space.subtype == "company":
            p_to.company_count -= 1
            p_from.company_count += 1
        if space.subtype == "bus":
            p_to.bus_count -= 1
            p_from.bus_count += 1
        space.owner = from_player

    _check_color_sets(state)
    _update_all_worth(state)

    events.append({
        "type": "trade_accepted",
        "fromPlayer": from_player,
        "toPlayer": to_player,
        "fromProperties": from_properties,
        "toProperties": to_properties,
        "fromMoney": from_money,
        "toMoney": to_money,
    })
    return events


def end_turn(state: GameState) -> list[dict]:
    """Human player ends their turn (used after doubles when they have an end-turn button)."""
    events: list[dict] = []
    _advance_turn(state)
    return events


def run_ai_turn(state: GameState) -> list[dict]:
    """Execute a full AI turn: roll, buy/pass, advance."""
    player = state.current_player()
    if player.is_human:
        return []
    events = roll_dice(state)
    return events
