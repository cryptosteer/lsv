__autor__ = 'Osnaider Miranda Caceres'

from functools import lru_cache


@lru_cache(maxsize=10)
def fibonacci_recursive(number):
    if number < 2:
        return number
    else:
        return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def fibonacci(number):
    a, b = 0, 1
    while number > 0 :
        print(a,end=', ')
        a, b = b, a + b
        number -= 1


print('Listing data of function fibonacci')
fibonacci(2000)

print('\n\nListing data of function fibonacci cached and recursive')
[print(fibonacci_recursive(number), end=', ') for number in range(10)]