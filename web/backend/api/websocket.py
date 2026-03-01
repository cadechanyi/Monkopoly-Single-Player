"""
WebSocket endpoint for the Monkopoly game.
Handles client actions, dispatches to game engine, runs AI turns automatically.
"""
from __future__ import annotations

import asyncio
import json

from fastapi import WebSocket, WebSocketDisconnect

from game import engine
from game.models import GameState

AI_TURN_DELAY = 1.5  # seconds between AI actions


async def game_websocket(websocket: WebSocket) -> None:
    await websocket.accept()
    state = engine.new_game()
    await _send_state(websocket, state)

    try:
        while True:
            raw = await websocket.receive_text()
            try:
                message = json.loads(raw)
            except json.JSONDecodeError:
                await websocket.send_json({"error": "Invalid JSON"})
                continue

            action = message.get("action")
            events = await _handle_action(state, action, message)

            await websocket.send_json({
                "type": "update",
                "events": events,
                "state": state.to_dict(),
            })

            # Run AI turns automatically after human actions resolve
            while state.phase == "ai_turn" and not state.game_over:
                await asyncio.sleep(AI_TURN_DELAY)
                ai_events = engine.run_ai_turn(state)

                await websocket.send_json({
                    "type": "update",
                    "events": ai_events,
                    "state": state.to_dict(),
                })

    except WebSocketDisconnect:
        pass


async def _handle_action(state: GameState, action: str, message: dict) -> list[dict]:
    if action == "new_game":
        new_state = engine.new_game()
        state.board = new_state.board
        state.players = new_state.players
        state.turn = new_state.turn
        state.doubles = new_state.doubles
        state.dice = new_state.dice
        state.phase = new_state.phase
        state.message = new_state.message
        state.chest_card = new_state.chest_card
        state.buy_property = new_state.buy_property
        state.game_over = new_state.game_over
        state._chest_cards = new_state._chest_cards
        return [{"type": "new_game"}]

    if action == "roll":
        if state.phase != "waiting_for_roll":
            return [{"type": "error", "message": "Cannot roll right now"}]
        return engine.roll_dice(state)

    if action == "buy":
        if state.phase != "waiting_for_buy":
            return [{"type": "error", "message": "No property to buy"}]
        return engine.buy_property(state)

    if action == "pass":
        if state.phase != "waiting_for_buy":
            return [{"type": "error", "message": "No property to pass on"}]
        return engine.pass_property(state)

    if action == "chest_ack":
        if state.phase != "waiting_for_chest":
            return [{"type": "error", "message": "No chest card to acknowledge"}]
        return engine.acknowledge_chest(state)

    if action == "mortgage":
        space_num = message.get("space")
        if space_num is None:
            return [{"type": "error", "message": "Missing space number"}]
        return engine.mortgage_property(state, space_num)

    if action == "add_house":
        space_num = message.get("space")
        if space_num is None:
            return [{"type": "error", "message": "Missing space number"}]
        return engine.add_house(state, space_num)

    if action == "remove_house":
        space_num = message.get("space")
        if space_num is None:
            return [{"type": "error", "message": "Missing space number"}]
        return engine.remove_house(state, space_num)

    if action == "propose_trade":
        return engine.execute_trade(
            state,
            from_player=message.get("fromPlayer", 0),
            to_player=message.get("toPlayer", 1),
            from_properties=message.get("fromProperties", []),
            to_properties=message.get("toProperties", []),
            from_money=message.get("fromMoney", 0),
            to_money=message.get("toMoney", 0),
        )

    if action == "end_turn":
        return engine.end_turn(state)

    if action == "end_game":
        state.game_over = True
        state.phase = "game_over"
        return [{"type": "game_over"}]

    return [{"type": "error", "message": f"Unknown action: {action}"}]


async def _send_state(websocket: WebSocket, state: GameState) -> None:
    await websocket.send_json({
        "type": "init",
        "state": state.to_dict(),
    })
