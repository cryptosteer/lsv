a = 1
b = 0
c = 0

for i in range(10):
	print(c, end=",")
	c = a + b	
	a = b
	b = c
	