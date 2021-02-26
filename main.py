from heapq import heappush, heappop
from collections import namedtuple
from typing import Dict, List, NamedTuple, Set, Tuple, Final
import load
from segment import Segment
from point import Point


def main():
    points: Final[Dict[int, Point]] = load.loadPoints()  # {id: Point}
    roads: Final[Dict[int, str]] = load.loadRoads()  # {id: str}
    load.loadSegments(points, roads)
    aStar(points)


def aStar(points: Dict[int, Point]) -> None:
    startPointID = int(input("Please input the ID of the starting point: "))
    while startPointID not in points.keys():
        print("Invalid key, try again")
        startPointID = int(input("Please input the ID of the starting point: "))
    endPointID = int(input("Please input the ID of the end point: "))
    while endPointID not in points.keys():
        print("Invalid key, try again")
        endPointID = int(input("Please input the ID of the starting point: "))
    startPoint, endPoint = points[startPointID], points[endPointID]

    SearchNode: NamedTuple[float, float, Segment] = namedtuple("SearchNode", ["estTotalCost", "costToStart", "segment"])
    frontier: List[SearchNode] = []
    heappush(frontier, SearchNode(startPoint.distanceTo(endPoint), 0, Segment(None, startPoint, 0)))
    visited: Set[Point] = {None}
    while frontier:
        searchNode = heappop(frontier)
        segment = searchNode.segment
        if not (segment.point1 in visited and segment.point2 in visited):
            curr = segment.point2 if segment.point1 in visited else segment.point1
            curr.prevSegment = segment
            visited.add(curr)
            if curr == endPoint:
                break
            costToStart = searchNode.costToStart + segment.length

            for potentialSeg in curr.segments:
                other = potentialSeg.point1 if potentialSeg.point1 != curr else potentialSeg.point2
                if other not in visited:
                    estTotalCost = costToStart + other.distanceTo(endPoint)
                    heappush(frontier, SearchNode(estTotalCost, costToStart, potentialSeg))
    printPath(startPoint, endPoint)


def printPath(startPoint: Point, endPoint: Point) -> None:
    trip: List[Tuple[str, float]] = []  # [(roadName, distance)]
    currPoint = endPoint
    currRoad = endPoint.prevSegment.road
    totalDist = roadLength = 0
    while currPoint != startPoint:
        segment = currPoint.prevSegment
        currPoint = segment.point1 if segment.point1 != currPoint else segment.point2
        if segment.road == currRoad:
            roadLength += segment.length
        else:
            trip.append(("Unknown road" if currRoad == "-" else currRoad, roadLength))
            totalDist += roadLength
            currRoad = segment.road
            roadLength = segment.length
    trip.append(("unknown road" if currRoad == "-" else currRoad, roadLength))
    totalDist += roadLength
    for road, length in reversed(trip):
        print("{} for {:.2f} km".format(road, length))
    print("total distance: {:.2f} km".format(totalDist))


if __name__ == "__main__":
    main()
