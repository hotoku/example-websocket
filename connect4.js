const PLAYER1 = "red";

const PLAYER2 = "yellow";

function createBoard(board) {
  // Generate board.
  for (let column = 0; column < 7; column++) {
    const columnElement = document.createElement("div");
    columnElement.className = "column";
    columnElement.dataset.column = column;
    for (let row = 0; row < 6; row++) {
      const cellElement = document.createElement("div");
      cellElement.className = "cell empty";
      cellElement.dataset.column = column;
      columnElement.append(cellElement);
    }
    board.append(columnElement);
  }
}

function initBoard(board) {
  // Inject stylesheet.
  const linkElement = document.createElement("link");
  linkElement.href = import.meta.url.replace(".js", ".css");
  linkElement.rel = "stylesheet";
  document.head.append(linkElement);
  createBoard(board);
}

function playMove(board, player, column, row) {
  // Check values of arguments.
  if (player !== PLAYER1 && player !== PLAYER2) {
    throw new Error(`player must be ${PLAYER1} or ${PLAYER2}.`);
  }
  const columnElement = board.querySelectorAll(".column")[column];
  if (columnElement === undefined) {
    throw new RangeError("column must be between 0 and 6.");
  }
  const cellElement = columnElement.querySelectorAll(".cell")[row];
  if (cellElement === undefined) {
    throw new RangeError("row must be between 0 and 5.");
  }
  // Place checker in cell.
  if (!cellElement.classList.replace("empty", player)) {
    throw new Error("cell must be empty.");
  }
}

function clearBoard(board) {
  for (let i = 0; i < 7; i++) {
    board.removeChild(board.childNodes[0]);
  }
  createBoard(board);
}

function fillBoard(board, moves) {
  for (const move of moves) {
    playMove(board, move.player, move.column, move.row);
  }
}

export { PLAYER1, PLAYER2, initBoard, clearBoard, playMove, fillBoard };
