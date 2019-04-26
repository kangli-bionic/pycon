from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
from common import timed

NUM_WORKERS = 12  # six cores


def fib(n):
    """Calculate the n-th element of Fibonacci."""
    a, b = 1, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return a


def fibs(n, x):
    """Calculate x copies of Fibonacci in series."""
    return [fib(n) for _ in range(x)]


def fibp(n, x, pool):
    """Calculate x copies of Fibonacci in parallel using the supplied executor."""
    return list(pool.map(fib, [n] * x))


with ThreadPool(NUM_WORKERS) as pool:
    assert fibs(10, 2) == fibp(10, 2, pool)
    timed(fibs, 5000, NUM_WORKERS)
    timed(fibp, 5000, NUM_WORKERS, pool)

with ProcessPool(NUM_WORKERS) as pool:
    assert fibs(10, 2) == fibp(10, 2, pool)
    timed(fibs, 5000, NUM_WORKERS)
    timed(fibp, 5000, NUM_WORKERS, pool)
