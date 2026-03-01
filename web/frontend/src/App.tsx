import { useMemo, useState } from "react";
import { useGameSocket } from "./hooks/useGameSocket";
import Board from "./components/Board";
import PlayerPanel from "./components/PlayerPanel";
import DiceDisplay from "./components/DiceDisplay";
import ControlPanel from "./components/ControlPanel";
import BuyModal from "./components/BuyModal";
import ChestModal from "./components/ChestModal";
import ManageModal from "./components/ManageModal";
import TradeModal from "./components/TradeModal";
import EndGameModal from "./components/EndGameModal";

export default function App() {
  const { gameState, events, connected, sendAction } = useGameSocket();
  const [showManage, setShowManage] = useState(false);
  const [showTrade, setShowTrade] = useState(false);

  const chestType = useMemo(() => {
    const chestEvent = events.find((e) => e.type === "chest_card");
    return (chestEvent?.chestType as string) ?? "baboon_bin";
  }, [events]);

  if (!connected || !gameState) {
    return (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          height: "100vh",
          gap: 16,
        }}
      >
        <div
          style={{
            width: 40,
            height: 40,
            border: "4px solid rgba(255,255,255,0.2)",
            borderTopColor: "#38a169",
            borderRadius: "50%",
            animation: "spin 0.8s linear infinite",
          }}
        />
        <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
        <div style={{ color: "#a0aec0", fontSize: 16 }}>Connecting to Monkopoly...</div>
      </div>
    );
  }

  const buySpace =
    gameState.phase === "waiting_for_buy" && gameState.buyProperty !== null
      ? gameState.board[gameState.buyProperty]
      : null;

  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: 24,
        height: "100vh",
        padding: 16,
      }}
    >
      {/* Player panels — fixed to screen corners */}
      <PlayerPanel players={gameState.players} currentTurn={gameState.turn} />

      {/* Board area */}
      <Board board={gameState.board} players={gameState.players} />

      {/* Side panel */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 20,
          alignItems: "center",
        }}
      >
        <DiceDisplay
          dice={gameState.dice as [number, number]}
          doubles={gameState.doubles}
          message={gameState.message}
        />
        <ControlPanel
          gameState={gameState}
          sendAction={sendAction}
          onManage={() => setShowManage(true)}
          onTrade={() => setShowTrade(true)}
        />
      </div>

      {/* Modals */}
      {buySpace && <BuyModal space={buySpace} sendAction={sendAction} />}

      {gameState.phase === "waiting_for_chest" && gameState.chestCard && (
        <ChestModal card={gameState.chestCard} chestType={chestType} sendAction={sendAction} />
      )}

      {showManage && (
        <ManageModal
          board={gameState.board}
          player={gameState.players[0]}
          sendAction={sendAction}
          onClose={() => setShowManage(false)}
        />
      )}

      {showTrade && (
        <TradeModal
          board={gameState.board}
          players={gameState.players}
          sendAction={sendAction}
          onClose={() => setShowTrade(false)}
        />
      )}

      {gameState.gameOver && (
        <EndGameModal players={gameState.players} sendAction={sendAction} />
      )}
    </div>
  );
}
