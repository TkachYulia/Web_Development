import math
a = int(input())
b = int(input())

x = range(a, b)
for i in x:
    d = int(math.sqrt(i))
    if d*d == i:
        print (i)