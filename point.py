from math import cos, asin, sqrt, pi
from typing import Final, List
import segment


class Point:
    def __init__(self, ID: int, lat: float, lon: float) -> None:
        self.ID: Final[int] = ID
        self.lat: Final[float] = lat
        self.lon: Final[float] = lon
        self.segments: List[segment.Segment] = []
        # following attributes only used during searching
        self.prevSegment: segment.Segment = None

    def distanceTo(self, other) -> float:
        rads = pi / 180  # radians per degree
        x = 0.5 - cos((other.lat - self.lat) * rads) / 2 + cos(self.lat * rads) * cos(other.lat * rads) \
            * (1 - cos((other.lon - self.lon) * rads)) / 2
        return 12742 * asin(sqrt(x))
