# Area Calculator Library

Библиотека для вычисления площади различных геометрических фигур, таких как круги и треугольники. Поддерживает добавление новых фигур

## Установка

Склонируйте репозиторий:

Установите зависимости:

```bash
make install
```

## Использование

Импортируйте необходимые классы и функции из библиотеки:

```python
from area_calc.area_calculator import calculate_area
from area_calc.shapes.Circle import Circle
from area_calc.shapes.Triangle import Triangle
```

Вычисление площади круга

```python
circle = Circle(5)
area = calculate_area(circle)
print(f"Area of the circle: {area}")
```

Вычисление площади треугольника

```pytjon
triangle = Triangle(3, 4, 5)
area = calculate_area(triangle)
print(f"Area of the triangle: {area}")
```

Проверка, является ли треугольник прямоугольным

```python
triangle = Triangle(3, 4, 5)
is_right = triangle.is_right_triangle()
print(f"Is the triangle right-angled? {is_right}")
```

### Добавление новой фигуры

Чтобы добавить новую фигуру, выполните следующие шаги:

- Создайте новый файл в папке *shapes*, например, *Rectangle.py.*
- Реализуйте класс фигуры, который наследует от Shape и реализует метод *get_area()* для вычисления площади.

Пример для прямоугольника:

```python
# area_calc/shapes/Rectangle.py

from area_calc.shapes.Shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
```

## Тестирование

Для запуска тестов выполните команду:

```bash
make test
```
