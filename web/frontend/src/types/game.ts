export interface BoardSpace {
  number: number;
  x: number;
  y: number;
  name: string;
  type: "go" | "property" | "chest" | "tax" | "jail" | "lunch" | "gotojail";
  subtype: "property" | "bus" | "company" | null;
  cost: number;
  rent: number[];
  houseCost: number;
  colorSet: number | null;
  owner: number | null;
  houses: number;
  mortgaged: boolean;
  completeSet: boolean;
}

export interface Player {
  number: number;
  color: string;
  color2: string;
  color3: string;
  isHuman: boolean;
  money: number;
  boardPosition: number;
  previousRoll: number;
  companyCount: number;
  busCount: number;
}

export interface ChestCard {
  text: string;
  moveTo: number | null;
  money: number;
}

export type GamePhase =
  | "waiting_for_roll"
  | "waiting_for_buy"
  | "waiting_for_chest"
  | "waiting_for_end_turn"
  | "ai_turn"
  | "game_over";

export interface GameState {
  turn: number;
  doubles: boolean;
  dice: [number, number];
  phase: GamePhase;
  message: string;
  chestCard: ChestCard | null;
  buyProperty: number | null;
  gameOver: boolean;
  players: Player[];
  board: BoardSpace[];
  availableActions: string[];
}

export interface GameEvent {
  type: string;
  [key: string]: unknown;
}

export interface ServerMessage {
  type: "init" | "update";
  state: GameState;
  events?: GameEvent[];
}

export type GameAction =
  | { action: "new_game" }
  | { action: "roll" }
  | { action: "buy" }
  | { action: "pass" }
  | { action: "chest_ack" }
  | { action: "mortgage"; space: number }
  | { action: "add_house"; space: number }
  | { action: "remove_house"; space: number }
  | {
      action: "propose_trade";
      fromPlayer: number;
      toPlayer: number;
      fromProperties: number[];
      toProperties: number[];
      fromMoney: number;
      toMoney: number;
    }
  | { action: "end_turn" }
  | { action: "end_game" };

// Color set number -> CSS color for board rendering
export const COLOR_SET_COLORS: Record<number, string> = {
  1: "#8B4513",
  2: "#87CEEB",
  3: "#DA70D6",
  4: "#FFA500",
  5: "#FF0000",
  6: "#FFFF00",
  7: "#008000",
  8: "#0000FF",
  9: "#FFFFFF",
  10: "#000000",
};

export const PROPERTY_IMAGES: Record<number, string> = {
  1: "caledon.png",
  3: "milton.png",
  5: "waynebus.png",
  6: "angola.png",
  8: "somalia.png",
  9: "chad.png",
  11: "scarborough.png",
  12: "pepsicompany.png",
  13: "Markham.png",
  14: "primarycampus.png",
  15: "jeffbus.png",
  16: "gcp.png",
  18: "mentorlobby.png",
  19: "bhavbarn.png",
  21: "mentorgym.png",
  23: "northkorea.png",
  24: "mentoroffice.png",
  25: "smithbus.png",
  26: "yehiapyramid.png",
  27: "egypt.png",
  28: "cokecompany.png",
  29: "landdownunder.png",
  31: "evancamp.png",
  32: "greenwood.png",
  34: "oakville.png",
  35: "danbus.png",
  37: "crystalcove.png",
  39: "jungleofmonkeys.png",
};

export const PLAYER_TOKEN_IMAGES: Record<number, string> = {
  0: "monkeyfaceblue4.png",
  1: "newmongreen.png",
  2: "newmonred.png",
  3: "newmonpink.png",
};
