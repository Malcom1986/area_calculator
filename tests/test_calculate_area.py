from area_calc.area_calculator import calculate_area
from area_calc.shapes.Circle import Circle
from area_calc.shapes.Triangle import Triangle
from pytest import approx


def test_circle_area():
    circle = Circle(5)
    assert calculate_area(circle) == approx(78.53981633974483)


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert calculate_area(triangle) == approx(6.0)


def test_triangle_is_right_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_triangle() is True

    triangle = Triangle(2, 2, 3)
    assert triangle.is_right_triangle() is False
