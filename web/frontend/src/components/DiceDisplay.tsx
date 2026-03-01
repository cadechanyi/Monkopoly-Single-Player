import { useEffect, useState } from "react";

interface DiceDisplayProps {
  dice: [number, number];
  doubles: boolean;
  message: string;
}

export default function DiceDisplay({ dice, doubles, message }: DiceDisplayProps) {
  const [animating, setAnimating] = useState(false);
  const [displayDice, setDisplayDice] = useState(dice);

  useEffect(() => {
    if (dice[0] === 0 && dice[1] === 0) return;

    setAnimating(true);
    let frame = 0;
    const interval = setInterval(() => {
      setDisplayDice([
        Math.ceil(Math.random() * 6),
        Math.ceil(Math.random() * 6),
      ] as [number, number]);
      frame++;
      if (frame >= 8) {
        clearInterval(interval);
        setDisplayDice(dice);
        setAnimating(false);
      }
    }, 100);

    return () => clearInterval(interval);
  }, [dice]);

  if (dice[0] === 0 && dice[1] === 0) return null;

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 6,
      }}
    >
      <div style={{ display: "flex", gap: 10 }}>
        {displayDice.map((d, i) => (
          <img
            key={i}
            src={`/images/dice${d}.png`}
            alt={`Dice ${d}`}
            style={{
              width: 48,
              height: 48,
              transition: animating ? "none" : "transform 0.2s",
              transform: animating ? `rotate(${Math.random() * 30 - 15}deg)` : "none",
            }}
            draggable={false}
          />
        ))}
      </div>
      {doubles && (
        <div
          style={{
            color: "#38a169",
            fontWeight: 800,
            fontSize: 18,
            textShadow: "0 0 8px rgba(56,161,105,0.5)",
          }}
        >
          DOUBLES!
        </div>
      )}
      {message && !doubles && (
        <div
          style={{
            color: message.startsWith("+") ? "#38a169" : "#e53e3e",
            fontWeight: 700,
            fontSize: 16,
          }}
        >
          {message}
        </div>
      )}
    </div>
  );
}
