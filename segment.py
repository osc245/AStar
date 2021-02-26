from typing import Final
from point import Point


class Segment:
    def __init__(self, point1: Point, point2: Point, length: float, road: str = None) -> None:
        self.point1: Final[Point] = point1
        self.point2: Final[Point] = point2
        self.length: Final[length] = length
        self.road: Final[str] = road

    # for priority queue
    def __lt__(self, other):
        (self.point1.ID, self.point2.ID) < (other.point1.ID, other.point2.ID)

    def __gt__(self, other):
        (self.point1.ID, self.point2.ID) > (other.point1.ID, other.point2.ID)

    def hash(self):
        hash(self.point1.ID + "-" + self.point2.ID)
