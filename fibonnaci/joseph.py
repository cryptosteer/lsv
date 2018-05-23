

def fibonaci(n):
    x=0
    y=1
    while x < n:
        print(x)
        x, y = y, x+y

fibonaci(5)