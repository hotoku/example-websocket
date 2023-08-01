import asyncio
import json
import logging
import secrets
from typing import Tuple

import websockets.server as ws

from connect4 import Connect4, PLAYER1, PLAYER2

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG
)
logging.getLogger("websockets.server").setLevel(logging.WARNING)

JOIN: dict[str, Tuple[Connect4, set[ws.WebSocketServerProtocol]]] = {}


async def start(websocket: ws.WebSocketServerProtocol):
    game = Connect4()
    connected = {websocket}

    join_key = secrets.token_urlsafe(12)
    JOIN[join_key] = game, connected
    try:
        event = {
            "type": "init",
            "join": join_key
        }
        await websocket.send(json.dumps(event))
        LOGGER.info("first player started game %s", id(game))

        while True:
            await play(websocket,
                       game,
                       PLAYER1,
                       connected)
    finally:
        del JOIN[join_key]


async def error(websocket: ws.WebSocketServerProtocol, message: str):
    event = {
        "type": "error",
        "message": message
    }
    await websocket.send(json.dumps(event))


async def play(websocket: ws.WebSocketServerProtocol, game: Connect4, player: str, connected: set[ws.WebSocketServerProtocol]):
    message = await websocket.recv()
    LOGGER.info("Player %s sent message %s", player, message)
    try:
        ret = game.play(json.loads(message), player)
        for ws in connected:
            await ws.send(json.dumps(ret))
        winner = game.judge()
        if winner:
            win = {
                "type": "win",
                "player": winner
            }
            for ws in connected:
                await ws.send(json.dumps(win))
    except Exception as e:
        await error(websocket, str(e))


async def join(websocket: ws.WebSocketServerProtocol, join_key: str):
    try:
        game, connected = JOIN[join_key]
    except KeyError:
        await error(websocket, "Game not found.")
        return

    connected.add(websocket)
    event = {
        "type": "board",
        "moves": game.history
    }
    await websocket.send(json.dumps(event))
    try:
        LOGGER.info("second player joined game %s", id(game))
        while True:
            await play(websocket,
                       game,
                       PLAYER2,
                       connected)
    finally:
        connected.remove(websocket)


async def handler(websocket: ws.WebSocketServerProtocol):
    message = await websocket.recv()
    event = json.loads(message)
    assert event["type"] == "init"

    if "join" in event:
        await join(websocket, event["join"])
    else:
        await start(websocket)


async def main():
    async with ws.serve(handler, "", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
