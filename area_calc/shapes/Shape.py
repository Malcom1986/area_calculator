from typing import Protocol


class Shape(Protocol):
    def get_area(self) -> float:
        ...
