import { fillBoard, clearBoard, initBoard, playMove } from "./connect4.js";

function showMessage(message) {
  setTimeout(() => alert(message), 50);
}

function receiveMessage(board, websocket) {
  websocket.addEventListener("message", ({ data }) => {
    const event = JSON.parse(data);
    console.log("receiveMessage: received", event);
    switch (event.type) {
      case "init":
        document.querySelector(".join").href = "?join=" + event.join;
        break;
      case "play":
        playMove(board, event.player, event.column, event.row);
        break;
      case "win":
        showMessage(`Player ${event.player} wins!`);
        break;
      case "error":
        showMessage(event.message);
        break;
      case "board":
        console.log("handling board", event);
        clearBoard(board);
        fillBoard(board, event.moves);
        break;
      default:
        throw new Error(`Unsupported event type: ${event.type}.`);
    }
  });
}

function initGame(websocket) {
  websocket.addEventListener("open", () => {
    const params = new URLSearchParams(window.location.search);
    const event = { type: "init" };
    if (params.has("join")) {
      event.join = params.get("join");
    }
    websocket.send(JSON.stringify(event));
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

function findBoadNode() {
  const board = document.querySelector(".board");
  return board;
}

window.addEventListener("DOMContentLoaded", () => {
  const board = findBoadNode();
  initBoard(board);
  const websocket = new WebSocket("ws://localhost:8002");
  initGame(websocket);
  sendMoves(board, websocket);
  receiveMessage(board, websocket);
  console.log(`DOMContentLoaded`);
});
