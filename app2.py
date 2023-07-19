import asyncio

from websockets.exceptions import ConnectionClosedOK
import websockets.server as ws


async def handler(websocket: ws.WebSocketServerProtocol):
    while True:
        try:
            message = await websocket.recv()
        except ConnectionClosedOK:
            break
        print(message)


async def main():
    async with ws.serve(handler, "", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
