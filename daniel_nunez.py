n, c, s, a, b=6,1,0,0,1
while c<n:
    s=a+b
    print(a, end=" ")
    a=b
    b=s
    c=c+1
