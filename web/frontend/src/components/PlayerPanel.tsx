import type { Player } from "../types/game";
import { PLAYER_TOKEN_IMAGES } from "../types/game";

interface PlayerPanelProps {
  players: Player[];
  currentTurn: number;
}

const PLAYER_NAMES: Record<number, string> = {
  0: "Blue Monkey",
  1: "Green Monkey",
  2: "Red Monkey",
  3: "Pink Monkey",
};

const POSITIONS: Record<number, React.CSSProperties> = {
  0: { top: 8, left: 8 },
  1: { top: 8, right: 8 },
  2: { bottom: 8, left: 8 },
  3: { bottom: 8, right: 8 },
};

export default function PlayerPanel({ players, currentTurn }: PlayerPanelProps) {
  return (
    <>
      {players.map((player) => (
        <div
          key={player.number}
          style={{
            position: "fixed",
            ...POSITIONS[player.number],
            display: "flex",
            alignItems: "center",
            gap: 10,
            padding: "8px 14px",
            borderRadius: 10,
            backgroundColor:
              currentTurn === player.number
                ? "rgba(255,255,255,0.15)"
                : "rgba(0,0,0,0.5)",
            border:
              currentTurn === player.number
                ? `2px solid ${player.color}`
                : "2px solid transparent",
            transition: "all 0.3s",
            zIndex: 50,
          }}
        >
          <img
            src={`/images/${PLAYER_TOKEN_IMAGES[player.number]}`}
            alt={PLAYER_NAMES[player.number]}
            style={{ width: 44, height: 40 }}
            draggable={false}
          />
          <div>
            <div
              style={{
                fontSize: 13,
                color: player.color,
                fontWeight: 800,
                textTransform: "uppercase",
              }}
            >
              {PLAYER_NAMES[player.number]}
            </div>
            <div
              style={{
                fontSize: 24,
                fontWeight: 800,
                color: "white",
                fontFamily: "monospace",
              }}
            >
              {player.money}
            </div>
          </div>
        </div>
      ))}
    </>
  );
}
