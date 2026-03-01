"""
Pure data models for the Monkopoly game. No UI dependencies.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .constants import (
    BOARD_SPACES,
    CHEST_CARDS,
    INITIAL_WORTH_DICT,
    NUM_PLAYERS,
    PLAYER_COLORS,
    STARTING_MONEY,
)


@dataclass
class BoardSpace:
    number: int
    x: int
    y: int
    name: str
    type: str  # "go", "property", "chest", "tax", "jail", "lunch", "gotojail"
    subtype: Optional[str]  # "property", "bus", "company", or None
    cost: int
    rent: list[int]  # rent0..rent5
    house_cost: int
    color_set: Optional[int]
    owner: Optional[int] = None  # player number, or None if unowned
    houses: int = 0
    mortgaged: bool = False
    complete_set: bool = False

    def to_dict(self) -> dict:
        return {
            "number": self.number,
            "x": self.x,
            "y": self.y,
            "name": self.name,
            "type": self.type,
            "subtype": self.subtype,
            "cost": self.cost,
            "rent": self.rent,
            "houseCost": self.house_cost,
            "colorSet": self.color_set,
            "owner": self.owner,
            "houses": self.houses,
            "mortgaged": self.mortgaged,
            "completeSet": self.complete_set,
        }


@dataclass
class ChestCard:
    text: str
    move_to: Optional[int]
    money: int

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "moveTo": self.move_to,
            "money": self.money,
        }


@dataclass
class Player:
    number: int
    color: str
    color2: str
    color3: str
    is_human: bool
    money: int
    board_position: int = 0
    previous_roll: int = 0
    company_count: int = 0
    bus_count: int = 0
    worth_dict: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "number": self.number,
            "color": self.color,
            "color2": self.color2,
            "color3": self.color3,
            "isHuman": self.is_human,
            "money": self.money,
            "boardPosition": self.board_position,
            "previousRoll": self.previous_roll,
            "companyCount": self.company_count,
            "busCount": self.bus_count,
        }


@dataclass
class GameState:
    board: list[BoardSpace]
    players: list[Player]
    turn: int = 0
    doubles: bool = False
    dice: list[int] = field(default_factory=lambda: [0, 0])
    phase: str = "waiting_for_roll"
    message: str = ""
    chest_card: Optional[ChestCard] = None
    buy_property: Optional[int] = None  # space number of property available to buy
    game_over: bool = False

    def to_dict(self) -> dict:
        return {
            "turn": self.turn,
            "doubles": self.doubles,
            "dice": self.dice,
            "phase": self.phase,
            "message": self.message,
            "chestCard": self.chest_card.to_dict() if self.chest_card else None,
            "buyProperty": self.buy_property,
            "gameOver": self.game_over,
            "players": [p.to_dict() for p in self.players],
            "board": [s.to_dict() for s in self.board],
            "availableActions": self._available_actions(),
        }

    def _available_actions(self) -> list[str]:
        if self.game_over:
            return ["new_game"]
        if self.phase == "waiting_for_roll":
            return ["roll", "manage", "trade", "end_game"]
        if self.phase == "waiting_for_buy":
            return ["buy", "pass"]
        if self.phase == "waiting_for_chest":
            return ["chest_ack"]
        if self.phase == "waiting_for_end_turn":
            return ["end_turn", "manage", "trade", "end_game"]
        if self.phase == "ai_turn":
            return []
        return []

    def current_player(self) -> Player:
        return self.players[self.turn]


def create_initial_state() -> GameState:
    board = []
    for space_data in BOARD_SPACES:
        board.append(BoardSpace(
            number=space_data["number"],
            x=space_data["x"],
            y=space_data["y"],
            name=space_data["name"],
            type=space_data["type"],
            subtype=space_data["subtype"],
            cost=space_data["cost"],
            rent=list(space_data["rent"]),
            house_cost=space_data["house_cost"],
            color_set=space_data["color_set"],
        ))

    players = []
    for pdata in PLAYER_COLORS[:NUM_PLAYERS]:
        players.append(Player(
            number=pdata["number"],
            color=pdata["color"],
            color2=pdata["color2"],
            color3=pdata["color3"],
            is_human=pdata["is_human"],
            money=STARTING_MONEY,
            worth_dict=dict(INITIAL_WORTH_DICT),
        ))

    chest_cards = [
        ChestCard(text=c["text"], move_to=c["move_to"], money=c["money"])
        for c in CHEST_CARDS
    ]

    state = GameState(board=board, players=players)
    state._chest_cards = chest_cards
    return state
