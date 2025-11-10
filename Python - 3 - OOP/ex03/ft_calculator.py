class calculator:
    """A calculator class"""

    def __init__(self, vec):
        """Init a calculator"""
        self.vec = vec

    def __add__(self, object) -> None:
        """Add a scalar to the vector"""
        print([x + object for x in self.vec])

    def __mul__(self, object) -> None:
        """Multiply the vector by a scalar"""
        print([x * object for x in self.vec])

    def __sub__(self, object) -> None:
        """Substract a scalar to the vector"""
        print([x - object for x in self.vec])

    def __truediv__(self, object) -> None:
        """Divide the vector by a scalar"""
        if object == 0:
            raise ZeroDivisionError("division by zero")
        print([x / object for x in self.vec])


def main():
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")


if __name__ == "__main__":
    main()
