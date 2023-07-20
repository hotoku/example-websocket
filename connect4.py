from dataclasses import dataclass
from enum import EnumMeta
from typing import Any


PLAYER1 = "red"
PLAYER2 = "yellow"


class Connect4:
    def __init__(self) -> None:
        # board[i][j]が、j行 i列
        self.board = [
            [None] * 6
        ] * 7
        self.currentPlayer = PLAYER1

    def play(self, msg: dict[str, Any]) -> dict[str, Any]:
        if msg.get("type") != "play":
            raise RuntimeError(f"unsupported type: {msg.get('type')}")
        col = msg["column"]
        return {
        }

    def find_bottom(self, col: int) -> int:
        cells = self.board[col]
        i = len(cells) - 1
        for i, c in enumerate(cells):
            if c is None:
                return i
        raise RuntimeError(f"column {col} is fulfilled.")
