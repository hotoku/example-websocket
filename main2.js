import { createBoard, playMove } from "./connect4.js";

function showMessage(message) {
  setTimeout(() => alert(message), 50);
}

function receiveMessage(board, websocket) {
  websocket.addEventListener("message", ({ data }) => {
    const event = JSON.parse(data);
    switch (event.type) {
      case "play":
        playMove(board, event.player, event.column, event.row);
        break;
      case "win":
        showMessage(`Player ${event.player} wins!`);
        break;
      case "error":
        showMessage(event.message);
        break;
      default:
        throw new Error(`Unsupported event type: ${event.type}.`);
    }
  });
}

function sendMoves(board, websocket) {
  board.addEventListener("click", ({ target }) => {
    const column = target.dataset.column;
    if (column === undefined) {
      return;
    }
    const event = {
      type: "play",
      column: parseInt(column, 10),
    };
    websocket.send(JSON.stringify(event));
  });
}

window.addEventListener("DOMContentLoaded", () => {
  const board = document.querySelector(".board");
  createBoard(board);
  const websocket = new WebSocket("ws://localhost:8002");
  sendMoves(board, websocket);
  receiveMessage(board, websocket);
  console.log(`DOMContentLoaded`);
});
