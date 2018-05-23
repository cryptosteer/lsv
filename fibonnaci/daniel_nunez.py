n, c, s, a, b= 2000, 1, 0, 0, 1
print("(", end="")
while c < n:
    s = a+b
    print(a, end="")
    a = b
    b = s
    c = c+1
    if c != n:
        print(",", end=" ")
print(")", end="")