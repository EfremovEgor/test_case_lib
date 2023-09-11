from abc import ABC, abstractmethod
from math import pi
from typing import Iterable


class Shape(ABC):
    @abstractmethod
    def area() -> float:
        """
        Calculates area of the shape

        Returns:
            Area of the shape
        """
        pass


class Circle(Shape):
    def __init__(self, radius: float | int) -> None:
        if not (isinstance(radius, float) or isinstance(radius, int)):
            raise TypeError(
                f"Radius cannot be type of {type(radius)}, only int or float"
            )
        if radius < 0:
            raise ValueError("Circle radius cannot be negative")

        self.radius = radius

    def area(self) -> float:
        return pi * self.radius**2


class Triangle(Shape):
    def __init__(
        self, side0: int | float, side1: int | float, side2: int | float
    ) -> None:
        for side in [side0, side1, side2]:
            if not (isinstance(side, float) or isinstance(side, int)):
                raise TypeError(
                    f"Side cannot be type of {type(side)}, only int or float"
                )
            if side < 0:
                raise ValueError("Triangle side cannot be negative")
        sides = sorted([side0, side1, side2])
        if sides[0] + sides[1] < sides[2]:
            raise ValueError(
                "One triangle side cannot be larger than the sum of the other two"
            )
        self.side0 = side0
        self.side1 = side1
        self.side2 = side2

    def is_right(self) -> bool:
        """
        Checks if triangle is right

        Returns:
            True if triangle is right else False
        """
        sides = sorted(side**2 for side in [self.side0, self.side1, self.side2])
        return sides[0] + sides[1] == sides[2]

    def area(self) -> float:
        perimeter = (self.side0 + self.side1 + self.side2) / 2
        return (
            perimeter
            * (perimeter - self.side0)
            * (perimeter - self.side1)
            * (perimeter - self.side2)
        ) ** 0.5


def multiple_shapes_area(shapes: Iterable[Shape]) -> list[float]:
    """
    Calculates areas of given shapes iterable

    Args:
        shapes (Iterable[Shape]): Shapes list

    Returns:
        List of areas
    """
    for shape in shapes:
        if not isinstance(shape, Shape):
            raise TypeError(
                f"Shapes items cannot be {type(shape)}, only instance or a subclass of Shape"
            )
    return [shape.area() for shape in shapes]
