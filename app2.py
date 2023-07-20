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
        try:
            message = await websocket.recv()
            ret = game.play(json.loads(message))
            await websocket.send(json.dumps(ret))
            winner = game.judge()
            if winner:
                await websocket.send(json.dumps(game.win(winner)))
        except RuntimeError as e:
            await websocket.send(json.dumps({
                "type": "error",
                "message": repr(e)
            }))


async def main():
    async with ws.serve(handler, "", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
