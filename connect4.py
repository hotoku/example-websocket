import logging
from typing import Any


LOGGER = logging.getLogger(__name__)

PLAYER1 = "red"
PLAYER2 = "yellow"


class Connect4:
    def __init__(self) -> None:
        # board[i][j]が、j行 i列
        self.board = [
            [None] * 6
            for _ in range(7)
        ]
        self.currentPlayer = PLAYER1

    def play(self, msg: dict[str, Any]) -> dict[str, Any]:
        if msg.get("type") != "play":
            raise RuntimeError(f"unsupported type: {msg.get('type')}")
        col = msg["column"]
        row = self.find_bottom(col)
        LOGGER.debug(f"col={col}, row={row}")
        self.board[col][row] = self.currentPlayer
        ret = {
            "type": "play",
            "player": self.currentPlayer,
            "column": col,
            "row": row
        }
        self.switch_player()
        return ret

    def switch_player(self) -> None:
        if self.currentPlayer == PLAYER1:
            self.currentPlayer = PLAYER2
        else:
            self.currentPlayer = PLAYER1

    def find_bottom(self, col: int) -> int:
        cells = self.board[col]
        i = len(cells) - 1
        for i, c in enumerate(cells):
            if c is None:
                return i
        raise RuntimeError(f"column {col} is fulfilled.")
