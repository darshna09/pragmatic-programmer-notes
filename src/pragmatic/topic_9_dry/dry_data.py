import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)


class Line:
    def __init__(self, start: Point, end: Point, length: float):
        self.start = start
        self.end = end
        self.length = length


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    line = Line(p1, p2, length=5.0)
    print("Initial length:", line.length)

    # External code breaks consistency
    line.start = Point(0, 0)
    line.end = Point(6, 8)

    print("After changing points:")
    print("Stored length (WRONG):", line.length)
