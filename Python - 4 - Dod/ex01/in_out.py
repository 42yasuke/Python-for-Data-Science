def square(x: int | float) -> int | float:
    """Calculate the square of a number."""
    return x * x


def pow(x: int | float) -> int | float:
    """Calculate the exponential of a number by himself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Apply the given function to the argument x and return the result."""
    count = 0

    def inner() -> float:
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner


if __name__ == "__main__":
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
