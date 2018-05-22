def Calculate(f):
    slots = {}
    def decorated_function(*args):
        slots[args] = f(*args) if args not in slots else slots[args]
        return slots[args]
    return decorated_function

@Calculate
def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    print(fib(20))
