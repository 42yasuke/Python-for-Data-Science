def testLists(height: list[int | float], lenght: int) -> bool:
    """
    Checks if a list is valid (type, length, and content).
    """
    if type(height) is not list:
        return False
    if len(height) != lenght:
        return False
    for i in height:
        if type(i) not in [int, float]:
            return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculates the BMI for each pair of height and weight.
    """
    if not testLists(height, len(weight)):
        raise AssertionError("The arguments are invalid")
    if not testLists(weight, len(height)):
        raise AssertionError("The arguments are invalid")
    res = []
    for h, w in zip(height, weight):
        res.append(w / (h * h))
    return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if each BMI value exceeds a given limit.
    """
    if not testLists(bmi, len(bmi)):
        raise AssertionError("The arguments are invalid")
    res = []
    for b in bmi:
        res.append(b >= limit)
    return res


def main():
    """
    Main function to test BMI calculations and limits.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == "__main__":
    main()
