import type { GameAction, GameState } from "../types/game";

interface ControlPanelProps {
  gameState: GameState;
  sendAction: (action: GameAction) => void;
  onManage: () => void;
  onTrade: () => void;
}

export default function ControlPanel({
  gameState,
  sendAction,
  onManage,
  onTrade,
}: ControlPanelProps) {
  const actions = gameState.availableActions;
  const isAiTurn = gameState.phase === "ai_turn";
  const currentPlayer = gameState.players[gameState.turn];

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: 8,
        padding: 16,
        borderRadius: 10,
        backgroundColor: "rgba(255,255,255,0.07)",
        minWidth: 180,
      }}
    >
      <div
        style={{
          fontSize: 12,
          color: isAiTurn ? "#f6ad55" : currentPlayer?.color ?? "white",
          fontWeight: 700,
          textTransform: "uppercase",
          textAlign: "center",
          marginBottom: 4,
        }}
      >
        {isAiTurn
          ? `AI ${gameState.turn} thinking...`
          : gameState.phase === "game_over"
            ? "Game Over"
            : "Your Turn"}
      </div>

      <button
        onClick={() => sendAction({ action: "roll" })}
        disabled={!actions.includes("roll")}
        style={{
          backgroundColor: "#38a169",
          color: "white",
          padding: "12px 24px",
          fontSize: 16,
        }}
      >
        Roll Dice
      </button>

      <button
        onClick={onManage}
        disabled={!actions.includes("manage")}
        style={{ backgroundColor: "#3182ce", color: "white" }}
      >
        Manage
      </button>

      <button
        onClick={onTrade}
        disabled={!actions.includes("trade")}
        style={{ backgroundColor: "#805ad5", color: "white" }}
      >
        Trade
      </button>

      <button
        onClick={() => sendAction({ action: "end_turn" })}
        disabled={!actions.includes("end_turn")}
        style={{ backgroundColor: "#718096", color: "white" }}
      >
        End Turn
      </button>

      <button
        onClick={() => sendAction({ action: "end_game" })}
        disabled={!actions.includes("end_game")}
        style={{ backgroundColor: "#e53e3e", color: "white" }}
      >
        End Game
      </button>

      {gameState.gameOver && (
        <button
          onClick={() => sendAction({ action: "new_game" })}
          style={{
            backgroundColor: "#38a169",
            color: "white",
            padding: "12px 24px",
            fontSize: 16,
            marginTop: 8,
          }}
        >
          New Game
        </button>
      )}
    </div>
  );
}
