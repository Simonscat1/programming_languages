import json

class PointError(Exception):
    ...

class Point:

    def __init__(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise PointError("x,y should be integer type")
        self.x = x
        self.y = y
    
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y  - other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            raise NotImplementedError
        return self.x == other.x and self.y == other.y

    def __neg__(self) -> "Point":
        return Point(-self.x, -self.y)

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

            
    def to_json(self) -> str:
        return json.dumps({"x": self.x, "y": self.y})

    @classmethod
    def from_json(cls: type, s: str) -> "Point":
        js = json.loads(s)
        return cls(int(js["x"]), int(js["y"]))

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"