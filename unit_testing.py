class Calc:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            raise ValueError('can not divide by zero!')
        return x / y


# Example 2
class Employee:
    """simple employee class"""
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self) -> str:
        return f'{self.first}.{self.last}@email.com'

    @property
    def full_name(self) -> str:
        return f'{self.first} {self.last}'

    def apply_raise(self) -> float:
        self.pay = int(self.pay * self.raise_amt)
        return self.pay
