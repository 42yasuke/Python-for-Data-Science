import numpy as np


def testArgs(family: list, start: int, end: int) -> bool:
    """
    Validates the arguments for the slice_me function.

    Parameters:
    - family (list): 2D list to validate.
    - start (int): Start index.
    - end (int): End index.

    Returns:
    - bool: True if arguments are valid, False otherwise.
    """
    if not isinstance(family, list):
        return False
    if not all(isinstance(row, list) for row in family):
        return False
    if not isinstance(start, int) or not isinstance(end, int):
        return False
    lenght = len(family[0])
    if not all(len(i) == lenght for i in family):
        return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """
    Converts a 2D list to a NumPy array, slices it,
    and returns the result as a list.

    Parameters:
    - family (list): 2D list to slice.
    - start (int): Start index.
    - end (int): End index.

    Returns:
    - list: Sliced portion of the array.
    """
    if not testArgs(family, start, end):
        raise AssertionError("The arguments are invalid")
    arr = np.array(family)
    print("My shape is :", arr.shape)
    arr = arr[start:end]
    print("My new shape is :", arr.shape)
    return arr.tolist()


def main():
    """
    Tests the slice_me function with example data.
    """
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == "__main__":
    main()
