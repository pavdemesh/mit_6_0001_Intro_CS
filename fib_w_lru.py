from functools import lru_cache


@lru_cache(maxsize=1000)
def fib_lru(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_lru(n - 1) + fib_lru(n - 2)


print(fib_lru(44))
