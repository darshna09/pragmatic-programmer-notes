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
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._recalculate_length()

    @property
    def start(self) -> Point:
        return self._start

    @start.setter
    def start(self, p: Point) -> None:
        self._start = p
        self._recalculate_length()

    @property
    def end(self) -> Point:
        return self._end

    @end.setter
    def end(self, p: Point) -> None:
        self._end = p
        self._recalculate_length()

    @property
    def length(self) -> float:
        return self._length

    def _recalculate_length(self) -> None:
        self._length = self._start.distance_to(self._end)


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    line = Line(p1, p2)
    print("Initial length:", line.length)

    # Updates go through the class, invariants preserved
    line.start = Point(0, 0)
    line.end = Point(6, 8)

    print("After changing points:")
    print("Recalculated length (CORRECT):", line.length)
