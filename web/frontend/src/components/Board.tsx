import type { BoardSpace, Player } from "../types/game";
import { PLAYER_TOKEN_IMAGES, COLOR_SET_COLORS } from "../types/game";

const BOARD_WIDTH = 737;
const BOARD_HEIGHT = 738;

interface BoardProps {
  board: BoardSpace[];
  players: Player[];
}

export default function Board({ board, players }: BoardProps) {
  return (
    <div
      className="board-container"
      style={{
        position: "relative",
        width: BOARD_WIDTH,
        height: BOARD_HEIGHT,
        flexShrink: 0,
      }}
    >
      <img
        src="/images/finalboard.png"
        alt="Monkopoly Board"
        style={{ width: BOARD_WIDTH, height: BOARD_HEIGHT, display: "block" }}
        draggable={false}
      />

      {/* Ownership indicators */}
      {board.map((space) => {
        if (space.owner === null || space.type !== "property") return null;
        const ownerPlayer = players[space.owner];
        if (!ownerPlayer) return null;

        const style = getOwnerIndicatorStyle(space, ownerPlayer.color);
        if (!style) return null;

        return (
          <div
            key={`owner-${space.number}`}
            style={{
              position: "absolute",
              backgroundColor: ownerPlayer.color,
              ...style,
            }}
          />
        );
      })}

      {/* Mortgaged labels */}
      {board.map((space) => {
        if (!space.mortgaged || space.owner === null) return null;
        const pos = getMortgagedPosition(space);
        if (!pos) return null;

        return (
          <div
            key={`mort-${space.number}`}
            style={{
              position: "absolute",
              left: pos.x,
              top: pos.y,
              backgroundColor: "#e53e3e",
              color: "white",
              fontSize: 9,
              fontWeight: 700,
              padding: "1px 3px",
              borderRadius: 2,
            }}
          >
            MORTGAGED
          </div>
        );
      })}

      {/* House indicators */}
      {board.map((space) => {
        if (space.houses <= 0 || space.subtype !== "property") return null;
        const pos = getHousePosition(space);
        if (!pos) return null;

        const isHotel = space.houses === 5;
        return (
          <div
            key={`house-${space.number}`}
            style={{
              position: "absolute",
              left: pos.x,
              top: pos.y,
              fontSize: 11,
              fontWeight: 700,
              color: isHotel ? "#e53e3e" : "#38a169",
              textShadow: "0 0 2px rgba(0,0,0,0.5)",
            }}
          >
            {isHotel ? "🏨" : "🌳".repeat(space.houses)}
          </div>
        );
      })}

      {/* Player tokens */}
      {players.map((player, idx) => {
        const space = board[player.boardPosition];
        if (!space) return null;
        const offset = getPlayerOffset(idx, players, player.boardPosition);
        return (
          <img
            key={`player-${player.number}`}
            src={`/images/${PLAYER_TOKEN_IMAGES[player.number]}`}
            alt={`Player ${player.number}`}
            style={{
              position: "absolute",
              left: space.x + offset.dx - 12,
              top: space.y + offset.dy - 12,
              width: 28,
              height: 26,
              transition: "left 0.4s ease, top 0.4s ease",
              zIndex: 10 + idx,
              filter: "drop-shadow(1px 1px 2px rgba(0,0,0,0.5))",
            }}
            draggable={false}
          />
        );
      })}
    </div>
  );
}

function getPlayerOffset(
  playerIdx: number,
  players: Player[],
  boardPosition: number
): { dx: number; dy: number } {
  const sameSpace = players.filter((p) => p.boardPosition === boardPosition);
  const posInGroup = sameSpace.findIndex((p) => p.number === playerIdx);

  // Spread tokens based on which side of the board they're on
  // so they don't overlap, matching the original tkinter layout
  if (boardPosition <= 10) {
    // Bottom row: spread vertically (upward)
    const offsets = [
      { dx: 0, dy: 0 },
      { dx: 0, dy: -25 },
      { dx: 0, dy: -50 },
      { dx: 0, dy: -75 },
    ];
    return offsets[posInGroup] || { dx: 0, dy: 0 };
  }
  if (boardPosition <= 20) {
    // Left column: spread horizontally (rightward)
    const offsets = [
      { dx: 0, dy: 0 },
      { dx: 25, dy: 0 },
      { dx: 50, dy: 0 },
      { dx: 75, dy: 0 },
    ];
    return offsets[posInGroup] || { dx: 0, dy: 0 };
  }
  if (boardPosition <= 30) {
    // Top row: spread vertically (downward)
    const offsets = [
      { dx: 0, dy: 0 },
      { dx: 0, dy: 25 },
      { dx: 0, dy: 50 },
      { dx: 0, dy: 75 },
    ];
    return offsets[posInGroup] || { dx: 0, dy: 0 };
  }
  // Right column: spread horizontally (leftward)
  const offsets = [
    { dx: 0, dy: 0 },
    { dx: -25, dy: 0 },
    { dx: -50, dy: 0 },
    { dx: -75, dy: 0 },
  ];
  return offsets[posInGroup] || { dx: 0, dy: 0 };
}

function getOwnerIndicatorStyle(
  space: BoardSpace,
  _color: string
): React.CSSProperties | null {
  const n = space.number;
  if (n < 10) return { left: space.x - 8, top: space.y - 100, width: 40, height: 4 };
  if (n > 10 && n < 20) return { left: space.x + 100, top: space.y - 10, width: 4, height: 30 };
  if (n > 20 && n < 30) return { left: space.x - 8, top: space.y + 100, width: 40, height: 4 };
  if (n > 30) return { left: space.x - 80, top: space.y - 10, width: 4, height: 30 };
  return null;
}

function getMortgagedPosition(space: BoardSpace): { x: number; y: number } | null {
  const n = space.number;
  if (n < 10) return { x: space.x - 10, y: space.y - 30 };
  if (n > 10 && n < 20) return { x: space.x + 10, y: space.y + 5 };
  if (n > 20 && n < 30) return { x: space.x - 15, y: space.y + 40 };
  if (n > 30) return { x: space.x - 80, y: space.y - 50 };
  return null;
}

function getHousePosition(space: BoardSpace): { x: number; y: number } | null {
  const n = space.number;
  if (n < 10) return { x: space.x + 15, y: space.y - 75 };
  if (n > 10 && n < 20) return { x: space.x + 80, y: space.y - 8 };
  if (n > 20 && n < 30) return { x: space.x + 10, y: space.y + 80 };
  if (n > 30) return { x: space.x - 60, y: space.y - 8 };
  return null;
}
