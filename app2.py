import asyncio
import json
import logging
import secrets

import websockets.server as ws

from connect4 import Connect4

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG
)
logging.getLogger("websockets.server").setLevel(logging.WARNING)

JOIN = {}


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
        LOGGER.info("first player started game", id(game))
        async for message in websocket:
            print("first player sent", message)
    finally:
        del JOIN[join_key]


async def handler(websocket: ws.WebSocketServerProtocol):
    message = await websocket.recv()
    event = json.loads(message)
    assert event["type"] == "init"
    await start(websocket)


async def main():
    async with ws.serve(handler, "", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
