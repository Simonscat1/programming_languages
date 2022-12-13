import json
from typing import Union

class PointError(Exception):
    ...

class Point:

    def __init__(self, x: Union[int,float], y: Union[int, float]) ->None:
        if not isinstance(x, (int,float)) or not isinstance(y, (int,float)):
            raise PointError("x, y should be integer type")
        self.x=x
        self.y=y
        
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            if hasattr(other, "__iter__"):    
                return self == Point(*other)
            else: 
                raise NotImplementedError
        return self.x == other.x and self.y == other.y
    
    def __neg__(self)-> "Point":
        return Point(-self.x, -self.y)
    
    def distance_to(self, other: "Point") -> float:
        return((self.x + other.x)**2 + (self.y-other.y)**2) ** 0.5
    
    def to_json(self) ->str:
        return json.dumps({"x":self.x, "y":self.x})
    
    @classmethod
    def from_json(cls: type, s: str) -> "Point":
        js = json.loads(s)
        return cls(float(js["x"]), float(js["y"], float(js["z"])))
    
    def __str__(self) ->str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    def __repr__(self) ->str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    
    def is_center(self) -> bool:
        return self == Point(0, 0)
    
    
    def is_file(self, file):
        file = "main.json"
        raise "work"
