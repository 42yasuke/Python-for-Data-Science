import numpy as np

def testLists(height: list[int | float], weight: list[int | float] = None) -> bool:
    return True

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if not testLists(height, weight):
         raise AssertionError("the arguments are bad")
    res = []
    for h, w in zip(height, weight):
        res.append(w / (h * h))
    return res

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not testLists(bmi):
         raise AssertionError("the arguments are bad")
    res = []
    for b in bmi:
        res.append(b >= limit)
    return res

def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    print("test")
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as ae:
        print(f"AssertionError: {ae}")


if __name__ == "__main__":
    main()
