import numpy as np


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
    arr = None
    try:
        arr = np.array(family)
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end must be integers.")
    except Exception as e:
        print("Error:", e)
        return []
    else:
        print("Original shape:", arr.shape)
        arr = arr[start:end]
        print("New shape:", arr.shape)
    return arr.tolist()


def main():
    """
    Tests the slice_me function with example data.
    """
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
