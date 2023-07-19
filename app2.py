import asyncio
import json
import logging

from websockets.exceptions import ConnectionClosedOK
import websockets.server as ws


LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG
)
logging.getLogger("websockets.server").setLevel(logging.WARNING)

PLAYER1 = "red"
PLAYER2 = "yellow"


async def handler(websocket: ws.WebSocketServerProtocol):
    for player, column, row in [
        (PLAYER1, 3, 0),
        (PLAYER2, 3, 1),
        (PLAYER1, 4, 0),
        (PLAYER2, 4, 1),
        (PLAYER1, 2, 0),
        (PLAYER2, 1, 0),
        (PLAYER1, 5, 0),
    ]:
        event = {
            "type": "play",
            "player": player,
            "column": column,
            "row": row
        }

        LOGGER.debug("handler: sending %s", event)
        await websocket.send(json.dumps(event))
        await asyncio.sleep(0.5)
    event = {
        "type": "win",
        "player": PLAYER1
    }
    await websocket.send(json.dumps(event))


async def main():
    async with ws.serve(handler, "", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
