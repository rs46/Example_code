"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attributes Definition
    size: str
    toppings: int
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings

    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza"""
        total: float = 0.0
        if self.size == 'large':
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total


def main():
    a_pizza: Pizza = Pizza('large', 3)                  # create Pizza object
    a_pizza.size = 'large'                              # set attribute size
    a_pizza.toppings = 3                                # set attribute topping
    a_pizza.extra_cheese = False                        # set attribute extra_cheese

    print(Pizza)                                        # <class '__main__.Pizza'>
    print(a_pizza)                                      # <__main__.Pizza object at (memory address)>
    print(a_pizza.size)                                 # large

    print(f'Price: ${a_pizza.price(1.05)}')             # method call, the me method is price()

    another_pizza: Pizza = Pizza('small', 0)
    another_pizza.extra_cheese = True
    print(another_pizza.size)
    print(f'Price: ${another_pizza.price(1.05)}')


if __name__ == '__main__':
    main()
