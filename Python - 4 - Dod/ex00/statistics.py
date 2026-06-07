def median(data: tuple) -> float:
    """Calculate the median of a list of numbers."""
    sorted_data = sorted(list(data))
    n = len(data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]


def mean(data: tuple) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(data) / len(data)


def quartile(data: tuple) -> list[float, float]:
    """Calculate the 1st and 3rd quartiles of a list of numbers."""
    sorted_data = sorted(list(data))
    n = len(data)
    q1 = sorted_data[int(0.25 * (n - 1))]
    q3 = sorted_data[int(0.75 * (n - 1))]
    return [q1, q3]


def variance(data: tuple) -> float:
    """Calculate the variance of a list of numbers."""
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / len(data)


def standard_deviation(data: tuple) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return variance(data) ** 0.5


def testArguments(args: tuple) -> bool:
    """Check if the arguments are valid for statistical calculations."""
    if len(args) < 1:
        return False
    for arg in args:
        if not isinstance(arg, (int, float)):
            return False
    return True


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate and print statistical measures
    based on the provided arguments and keyword arguments."""
    for value in kwargs.values():
        if not testArguments(args):
            print("ERROR")
            continue
        match value:
            case "mean":
                print(f"mean: {mean(args)}")
            case "median":
                print(f"median: {median(args)}")
            case "quartile":
                print(f"quartile: {quartile(args)}")
            case "std":
                print(f"std: {standard_deviation(args)}")
            case "var":
                print(f"var: {variance(args)}")
            case _:
                pass


if __name__ == "__main__":
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
