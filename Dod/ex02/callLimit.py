from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return
            return function(*args, **kwds)
        return limit_function
    return callLimiter


def main() -> None:
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
