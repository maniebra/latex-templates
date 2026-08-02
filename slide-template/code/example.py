from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Nothing clever. The cache does the work."""
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(10)])
