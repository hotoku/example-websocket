import logging
from typing import Any, Literal


LOGGER = logging.getLogger(__name__)

PLAYER1 = "red"
PLAYER2 = "yellow"

Player = Literal["red"] | Literal["yellow"]


class Connect4:
    rownum = 6
    colnum = 7

    def __init__(self) -> None:
        # board[i][j]が、j行 i列
        # i.e. board[col][row]でアクセス
        self.board = [
            [None] * self.rownum
            for _ in range(self.colnum)
        ]
        self.currentPlayer = PLAYER1

    def play(self, msg: dict[str, Any], player: Player) -> dict[str, Any]:
        if msg.get("type") != "play":
            raise RuntimeError(f"unsupported type: {msg.get('type')}")
        if player != self.currentPlayer:
            raise RuntimeError("it is not your turn")
        col = msg["column"]
        row = self.find_bottom(col)
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

    def judge(self) -> str | None:
        if self.judge1(PLAYER1):
            return PLAYER1
        elif self.judge1(PLAYER2):
            return PLAYER2
        else:
            return None

    def judge1(self, player: str) -> bool:
        for r in range(self.rownum):
            for c in range(self.colnum):
                ret1 = self.dfs(player, c, r, 0, 1, 1)
                ret2 = self.dfs(player, c, r, 1, 0, 1)
                ret3 = self.dfs(player, c, r, 1, 1, 1)
                if ret1 or ret2 or ret3:
                    return True
        return False

    def dfs(self, player: str, col: int, row: int, dcol: int, drow: int, depth: int) -> bool:
        try:
            if col == self.colnum or row == self.rownum:
                return False
            if self.board[col][row] != player:
                return False
            if depth == 4:
                return True
            return self.dfs(player, col + dcol, row + drow, dcol, drow, depth + 1)
        except Exception as e:
            import pdb
            pdb.set_trace()
            raise e

    def win(self, winner: str) -> dict[str, Any]:
        return {
            "type": "win",
            "player": winner
        }
