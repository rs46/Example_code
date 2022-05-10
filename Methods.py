from __future__ import annotations

# Module with different kind of examples of methods


# noinspection PyCompatibility
class Person:
    name: str
    age: int = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hello(self) -> None:
        print(f'hello {self.name}')

    def __repr__(self) -> str:
        return f'{self.age}'


# noinspection PyCompatibility
class Point:

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y args."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Special method to represent object as string"""
        return f'{self.x},{self.y}'

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operation for Point * float"""
        print('__mul__ was called')
        return Point(self.x * factor, self.y * factor)

    def __add__(self, rhs: Point) -> Point:
        """Overload the add operation for Point + float"""
        print('__add__ was called')
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscription notation"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            return IndexError


# noinspection PyCompatibility
def main() -> None:
    a: Point = Point(1.5, 1.5)
    b: Point = a * 2.0
    c: Point = a + b

    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')

    # make use of the __getitem__
    print(a[0])
    print(a[1])


if __name__ == '__main__':
    main()
