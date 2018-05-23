print(0)
a = 1
b = 0
c = 0

for i in range(4000):
    c = a + b
    a = b
    b = c
    print(c)