"""
AI decision logic — ported from Objects.py player methods.
Pure logic, no UI dependencies.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from .constants import BUS_SPACES, TWO_PROPERTY_SETS

if TYPE_CHECKING:
    from .models import BoardSpace, GameState, Player


def set_property_worth(player: Player, board: list[BoardSpace]) -> None:
    """Recalculate the AI worth_dict for a player based on current board ownership."""
    for item in player.worth_dict:
        owned_in_set = 0
        target_space = board[item]
        for space in board:
            if space.color_set == target_space.color_set and space.color_set is not None:
                if space.owner == player.number and space.owner is not None:
                    owned_in_set += 1
                    if space.number in [1, 3, 37, 39]:
                        owned_in_set *= 2

        if item not in BUS_SPACES:
            player.worth_dict[item] = (board[item].cost / 10) * ((2 ** owned_in_set) ** owned_in_set)
        else:
            player.worth_dict[item] = (board[item].cost / 10) * (2 ** owned_in_set)


def ai_property_buy_check(player: Player, space_num: int, board: list[BoardSpace]) -> bool:
    """Decide whether an AI player should buy a property. Returns True to buy."""
    if space_num not in player.worth_dict:
        return player.money >= board[space_num].cost
    buy_value = player.worth_dict[space_num] * (player.money - board[space_num].cost)
    return buy_value >= 2200


def ai_trade_check(
    state: GameState,
    from_player: int,
    to_player: int,
    from_properties: list[int],
    to_properties: list[int],
    from_money: int,
    to_money: int,
) -> bool:
    """
    Decide whether the AI (to_player) accepts a trade.
    Ported from player.ai_trade_check in Objects.py.
    """
    board = state.board
    ai = state.players[to_player]

    worth_from = 0.0
    worth_to = 0.0

    # Value of money being offered
    if from_money > 0:
        money_val = from_money * 5 // ((max(ai.money, 100) ** 0.5) ** 0.5)
        worth_from += money_val
    if to_money > 0:
        money_val = to_money * 5 // ((min(ai.money, 100) ** 0.5) ** 0.5)
        worth_to += money_val

    # Value properties being given to AI (from_properties)
    for sp_num in from_properties:
        space = board[sp_num]
        worth_from += space.cost / 2
        owned_in_set = 0
        for other in board:
            if other.color_set == space.color_set and other.color_set is not None:
                if other.owner == to_player and other.number != sp_num:
                    owned_in_set += 1
                    if other.number in [1, 3, 37, 39]:
                        owned_in_set *= 2
        for other_sp in from_properties:
            if other_sp != sp_num and board[other_sp].color_set == space.color_set:
                owned_in_set += 1
                if other_sp in [1, 3, 37, 39]:
                    owned_in_set *= 2

        if sp_num not in BUS_SPACES:
            worth_from += (space.cost / 10) * ((2 ** owned_in_set) ** owned_in_set)
        else:
            worth_from += (space.cost / 10) * (2 ** owned_in_set)

    # Value properties AI is giving away (to_properties)
    for sp_num in to_properties:
        space = board[sp_num]
        worth_to += space.cost / 2
        owned_in_set = 0
        for other in board:
            if other.color_set == space.color_set and other.color_set is not None:
                if other.owner == from_player and other.number != sp_num:
                    owned_in_set += 1
                    if other.number in [1, 3, 37, 39]:
                        owned_in_set *= 2
        for other_sp in to_properties:
            if other_sp != sp_num and board[other_sp].color_set == space.color_set:
                owned_in_set += 1
                if other_sp in [1, 3, 37, 39]:
                    owned_in_set *= 2

        if sp_num not in BUS_SPACES:
            worth_to += (space.cost / 10) * ((2 ** owned_in_set) ** owned_in_set)
        else:
            worth_to += (space.cost / 10) * (2 ** owned_in_set)

    return worth_from >= worth_to
