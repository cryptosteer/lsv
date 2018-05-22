# Fibonacci
def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n  = 150
for i in range(n):
    print(fibonacci(i))
