def callLimit(limit: int):
    """Wrapper that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return None
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter


def main():
    """main is the main function that tests the callLimit wrapper."""
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
