print(0)
print(1)
a = 1
b = 0
c = 0

for i in range(10):
    c = a + b
    a = b
    b = c
    print(c)