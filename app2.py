import asyncio

import websockets.server as ws


async def handler(websocket: ws.WebSocketServerProtocol):
    while True:
        message = await websocket.recv()
        print(message)


async def main():
    async with ws.serve(handler, "", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
