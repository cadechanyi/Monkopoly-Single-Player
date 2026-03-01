import { useCallback, useEffect, useRef, useState } from "react";
import type { GameAction, GameEvent, GameState, ServerMessage } from "../types/game";

const WS_URL =
  (window.location.protocol === "https:" ? "wss://" : "ws://") +
  window.location.host +
  "/ws/game";

export function useGameSocket() {
  const [gameState, setGameState] = useState<GameState | null>(null);
  const [events, setEvents] = useState<GameEvent[]>([]);
  const [connected, setConnected] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimer = useRef<ReturnType<typeof setTimeout>>();

  const connect = useCallback(() => {
    if (wsRef.current?.readyState === WebSocket.OPEN) return;

    const ws = new WebSocket(WS_URL);
    wsRef.current = ws;

    ws.onopen = () => setConnected(true);

    ws.onmessage = (event) => {
      const msg: ServerMessage = JSON.parse(event.data);
      if (msg.state) setGameState(msg.state);
      if (msg.events) setEvents(msg.events);
    };

    ws.onclose = () => {
      setConnected(false);
      reconnectTimer.current = setTimeout(connect, 2000);
    };

    ws.onerror = () => ws.close();
  }, []);

  useEffect(() => {
    connect();
    return () => {
      clearTimeout(reconnectTimer.current);
      wsRef.current?.close();
    };
  }, [connect]);

  const sendAction = useCallback((action: GameAction) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(action));
    }
  }, []);

  return { gameState, events, connected, sendAction };
}
