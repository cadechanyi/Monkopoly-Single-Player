import { useState } from "react";
import type { BoardSpace, GameAction, Player } from "../types/game";
import { PROPERTY_IMAGES } from "../types/game";

interface TradeModalProps {
  board: BoardSpace[];
  players: Player[];
  sendAction: (action: GameAction) => void;
  onClose: () => void;
}

export default function TradeModal({ board, players, sendAction, onClose }: TradeModalProps) {
  const humanPlayer = players[0];
  const aiPlayers = players.filter((p) => !p.isHuman);

  const [selectedOpponent, setSelectedOpponent] = useState<number | null>(null);
  const [fromProperties, setFromProperties] = useState<number[]>([]);
  const [toProperties, setToProperties] = useState<number[]>([]);
  const [fromMoney, setFromMoney] = useState(0);
  const [toMoney, setToMoney] = useState(0);

  const myProperties = board.filter(
    (s) => s.owner === 0 && s.type === "property" && s.houses === 0
  );
  const opponentProperties = selectedOpponent !== null
    ? board.filter((s) => s.owner === selectedOpponent && s.type === "property" && s.houses === 0)
    : [];

  const toggleFrom = (num: number) => {
    setFromProperties((prev) =>
      prev.includes(num) ? prev.filter((n) => n !== num) : [...prev, num]
    );
  };

  const toggleTo = (num: number) => {
    setToProperties((prev) =>
      prev.includes(num) ? prev.filter((n) => n !== num) : [...prev, num]
    );
  };

  const canPropose =
    selectedOpponent !== null &&
    (fromProperties.length > 0 || fromMoney > 0) &&
    (toProperties.length > 0 || toMoney > 0);

  const proposeTrade = () => {
    if (selectedOpponent === null) return;
    sendAction({
      action: "propose_trade",
      fromPlayer: 0,
      toPlayer: selectedOpponent,
      fromProperties,
      toProperties,
      fromMoney,
      toMoney,
    });
    onClose();
  };

  return (
    <div style={overlayStyle}>
      <div style={modalStyle}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", width: "100%" }}>
          <h2 style={{ margin: 0, fontSize: 20, color: "white" }}>Trade</h2>
          <button onClick={onClose} style={{ backgroundColor: "#718096", color: "white", padding: "6px 14px", fontSize: 13 }}>
            Close
          </button>
        </div>

        {/* Opponent selection */}
        <div>
          <div style={{ fontSize: 12, color: "#a0aec0", marginBottom: 6 }}>Trade with:</div>
          <div style={{ display: "flex", gap: 8 }}>
            {aiPlayers.map((p) => {
              const hasProps = board.some((s) => s.owner === p.number && s.houses === 0);
              return (
                <button
                  key={p.number}
                  onClick={() => {
                    setSelectedOpponent(p.number);
                    setToProperties([]);
                    setToMoney(0);
                  }}
                  disabled={!hasProps}
                  style={{
                    backgroundColor: selectedOpponent === p.number ? p.color : "rgba(255,255,255,0.1)",
                    color: selectedOpponent === p.number ? "black" : p.color,
                    padding: "8px 16px",
                    fontWeight: 700,
                  }}
                >
                  AI {p.number} (${p.money})
                </button>
              );
            })}
          </div>
        </div>

        {selectedOpponent !== null && (
          <div style={{ display: "flex", gap: 20, width: "100%" }}>
            {/* Your side */}
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#68d391", marginBottom: 8 }}>
                You Give:
              </div>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 8 }}>
                {myProperties.map((s) => (
                  <PropertyChip
                    key={s.number}
                    space={s}
                    selected={fromProperties.includes(s.number)}
                    onClick={() => toggleFrom(s.number)}
                  />
                ))}
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
                <span style={{ color: "#a0aec0", fontSize: 13 }}>$</span>
                <input
                  type="number"
                  min={0}
                  max={humanPlayer.money}
                  value={fromMoney}
                  onChange={(e) => setFromMoney(Math.min(humanPlayer.money, Math.max(0, Number(e.target.value))))}
                  style={inputStyle}
                />
              </div>
            </div>

            {/* Opponent side */}
            <div style={{ flex: 1 }}>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#fc8181", marginBottom: 8 }}>
                You Get:
              </div>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 8 }}>
                {opponentProperties.map((s) => (
                  <PropertyChip
                    key={s.number}
                    space={s}
                    selected={toProperties.includes(s.number)}
                    onClick={() => toggleTo(s.number)}
                  />
                ))}
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
                <span style={{ color: "#a0aec0", fontSize: 13 }}>$</span>
                <input
                  type="number"
                  min={0}
                  max={players[selectedOpponent]?.money ?? 0}
                  value={toMoney}
                  onChange={(e) =>
                    setToMoney(Math.min(players[selectedOpponent]?.money ?? 0, Math.max(0, Number(e.target.value))))
                  }
                  style={inputStyle}
                />
              </div>
            </div>
          </div>
        )}

        <button
          onClick={proposeTrade}
          disabled={!canPropose}
          style={{
            backgroundColor: "#805ad5",
            color: "white",
            padding: "12px 32px",
            fontSize: 16,
            alignSelf: "center",
          }}
        >
          Propose Trade
        </button>
      </div>
    </div>
  );
}

function PropertyChip({
  space,
  selected,
  onClick,
}: {
  space: BoardSpace;
  selected: boolean;
  onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      style={{
        backgroundColor: selected ? "rgba(255,255,255,0.25)" : "rgba(255,255,255,0.06)",
        border: selected ? "2px solid #f6e05e" : "2px solid transparent",
        borderRadius: 6,
        padding: "4px 8px",
        color: "white",
        fontSize: 11,
        display: "flex",
        alignItems: "center",
        gap: 4,
      }}
    >
      {space.mortgaged && <span style={{ color: "#fc8181", fontSize: 9 }}>M</span>}
      {space.name}
    </button>
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
  padding: 24,
  display: "flex",
  flexDirection: "column",
  gap: 16,
  boxShadow: "0 8px 32px rgba(0,0,0,0.4)",
  maxWidth: 700,
  maxHeight: "85vh",
  minWidth: 500,
};

const inputStyle: React.CSSProperties = {
  backgroundColor: "rgba(255,255,255,0.1)",
  border: "1px solid rgba(255,255,255,0.2)",
  borderRadius: 6,
  color: "white",
  padding: "6px 10px",
  fontSize: 14,
  width: 100,
};
