import type { BoardSpace, GameAction } from "../types/game";
import { PROPERTY_IMAGES } from "../types/game";

interface BuyModalProps {
  space: BoardSpace;
  sendAction: (action: GameAction) => void;
}

export default function BuyModal({ space, sendAction }: BuyModalProps) {
  const imageFile = PROPERTY_IMAGES[space.number];

  return (
    <div style={overlayStyle}>
      <div style={modalStyle}>
        <h2 style={{ margin: 0, fontSize: 20, color: "white" }}>{space.name}</h2>
        <div style={{ fontSize: 36, fontWeight: 800, color: "#f6e05e", fontFamily: "monospace" }}>
          ${space.cost}
        </div>

        {imageFile && (
          <img
            src={`/images/${imageFile}`}
            alt={space.name}
            style={{ maxWidth: 200, maxHeight: 280, borderRadius: 6 }}
            draggable={false}
          />
        )}

        <div style={{ display: "flex", gap: 16, marginTop: 12 }}>
          <button
            onClick={() => sendAction({ action: "buy" })}
            style={{
              backgroundColor: "#38a169",
              color: "white",
              padding: "14px 32px",
              fontSize: 18,
            }}
          >
            Buy
          </button>
          <button
            onClick={() => sendAction({ action: "pass" })}
            style={{
              backgroundColor: "#e53e3e",
              color: "white",
              padding: "14px 32px",
              fontSize: 18,
            }}
          >
            Pass
          </button>
        </div>
      </div>
    </div>
  );
}

const overlayStyle: React.CSSProperties = {
  position: "fixed",
  inset: 0,
  backgroundColor: "rgba(0,0,0,0.6)",
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
  alignItems: "center",
  gap: 12,
  boxShadow: "0 8px 32px rgba(0,0,0,0.4)",
  maxWidth: 400,
};
