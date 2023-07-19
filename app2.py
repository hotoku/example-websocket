import asyncio
import json
import logging

from websockets.exceptions import ConnectionClosedOK
import websockets.server as ws

from connect4 import PLAYER1, PLAYER2, Connect4

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG
)
logging.getLogger("websockets.server").setLevel(logging.WARNING)


async def handler(websocket: ws.WebSocketServerProtocol):
    game = Connect4()
    while True:
        message = await websocket.recv()


async def main():
    async with ws.serve(handler, "", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
