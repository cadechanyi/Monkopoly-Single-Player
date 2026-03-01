import type { GameAction, Player } from "../types/game";

interface EndGameModalProps {
  players: Player[];
  sendAction: (action: GameAction) => void;
}

export default function EndGameModal({ players, sendAction }: EndGameModalProps) {
  const sorted = [...players].sort((a, b) => b.money - a.money);

  return (
    <div style={overlayStyle}>
      <div style={modalStyle}>
        <h2 style={{ margin: 0, fontSize: 24, color: "white", textAlign: "center" }}>
          Game Over
        </h2>

        <div style={{ display: "flex", flexDirection: "column", gap: 10, width: "100%" }}>
          {sorted.map((player, idx) => (
            <div
              key={player.number}
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "10px 16px",
                borderRadius: 8,
                backgroundColor:
                  idx === 0 ? "rgba(246,224,94,0.15)" : "rgba(255,255,255,0.05)",
                border: idx === 0 ? "2px solid #f6e05e" : "2px solid transparent",
              }}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                <span style={{ fontSize: 20, fontWeight: 800, color: idx === 0 ? "#f6e05e" : "#a0aec0" }}>
                  #{idx + 1}
                </span>
                <span style={{ color: player.color, fontWeight: 700 }}>
                  {player.isHuman ? "You" : `AI ${player.number}`}
                </span>
              </div>
              <span style={{ fontSize: 20, fontWeight: 800, color: "white", fontFamily: "monospace" }}>
                ${player.money}
              </span>
            </div>
          ))}
        </div>

        <button
          onClick={() => sendAction({ action: "new_game" })}
          style={{
            backgroundColor: "#38a169",
            color: "white",
            padding: "14px 32px",
            fontSize: 18,
            alignSelf: "center",
            marginTop: 8,
          }}
        >
          Play Again
        </button>
      </div>
    </div>
  );
}

const overlayStyle: React.CSSProperties = {
  position: "fixed",
  inset: 0,
  backgroundColor: "rgba(0,0,0,0.7)",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  zIndex: 100,
};

const modalStyle: React.CSSProperties = {
  backgroundColor: "#2d3748",
  borderRadius: 12,
  padding: 28,
  display: "flex",
  flexDirection: "column",
  gap: 16,
  boxShadow: "0 8px 32px rgba(0,0,0,0.4)",
  maxWidth: 400,
  minWidth: 320,
};
