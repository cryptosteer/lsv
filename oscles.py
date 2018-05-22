from functools import lru_cache


@lru_cache(maxsize=10)
def fibonacci(number):
    if number < 2:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


def main():
    print([fibonacci(number) for number in range(2000)])


if __name__ == '__main__':
    main()
