import math

from area_calc.shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)
