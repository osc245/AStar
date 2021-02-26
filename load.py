from typing import Dict
from re import split
from segment import Segment
from point import Point


def loadPoints() -> Dict[int, Point]:
    points = dict()
    try:
        with open("data/points.tab", 'r') as f:
            for line in f:
                data = line.strip().split()
                pointID = int(data[0])
                lat, lon = float(data[1]), float(data[2])
                points[pointID] = Point(pointID, lat, lon)
    except FileNotFoundError as e:
        print("Loading data from the point file failed:", e)
    except RuntimeError as e:
        print("An error occurred while reading the point data file:", e)
    return points


def loadRoads() -> Dict[int, str]:
    roads = dict()
    try:
        with open("data/roads.tab", 'r') as f:
            f.readline()
            for line in f:
                data = split("[\t]+", line.strip())
                roadID = int(data[0])
                name = data[2]
                roads[roadID] = name
    except FileNotFoundError as e:
        print("Loading data from the road file failed:", e)
    except RuntimeError as e:
        print("An error occurred while reading the road data file:", e)
    return roads


def loadSegments(points: Dict[int, Point], roads: Dict[int, str]) -> None:
    try:
        with open("data/segments.tab", 'r') as f:
            f.readline()
            for line in f:
                data = line.strip().split()
                roadID = int(data[0])
                length = float(data[1])
                point1 = points[int(data[2])]
                point2 = points[int(data[3])]
                segment = Segment(point1, point2, length, roads[roadID])
                point1.segments.append(segment)
                point2.segments.append(segment)
    except FileNotFoundError as e:
        print("Loading data from the segment file failed:", e)
    except RuntimeError as e:
        print("An error occurred while reading the segment data file:", e)