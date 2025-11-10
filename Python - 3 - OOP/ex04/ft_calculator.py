class calculator:
    """A calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiply two vectors"""
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(f'Dot product is: {result}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors"""
        print(f'Add Vector is: {[float(x + y) for x, y in zip(V1, V2)]}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substract two vectors"""
        print(f'Sous Vector is: {[float(x - y) for x, y in zip(V1, V2)]}')


def main():
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
