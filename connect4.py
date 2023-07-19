from typing import Any


PLAYER1 = "red"
PLAYER2 = "yellow"


class Connect4:
    def __init__(self) -> None:
        self.board = [
            [None] * 7
        ] * 6

    def play(self, msg: dict[str, Any]) -> dict[str, Any]:
        return {}
