import sys
import time
import pprint

"""
Recursive decorator with fixed recursion limit
"""
sys.setrecursionlimit(40000)


def Calculate(f):
    slots = {}

    def decorated_function(*args):
        slots[args] = f(*args) if args not in slots else slots[args]
        return slots[args]

    return decorated_function


@Calculate
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


"""
Generator fibo
"""


def fib_even_gen(n):
    a = 0
    b = 1
    c = 1
    yield a
    while c < n:
        a = b
        b = a + b
        if a % 2 == 0:
            yield a
            c += 1
    return a


if __name__ == '__main__':
    # Decorator with recursion list comprehension
    start4 = time.perf_counter()
    l = [fib(a) for a in range(0, 20000)]
    print(l)
    end4 = time.perf_counter()
    print("=" * 30 + "\n", "Recusive decorator en {} segundos".format(end4 - start4))

    # Fibo with generator
    start2 = time.perf_counter()
    enumerate(fib_even_gen(20000), 0)
    end2 = time.perf_counter()
    print("=" * 30 + "\n", "Generador en {} segundos".format(end2 - start2))

    # Decorator with recursion limit fixed
    start = time.perf_counter()
    fib(332)
    print()
    fib(664)
    end = time.perf_counter()
    print("=" * 30 + "\n", "Recusive decorator en {} segundos".format(end - start))
