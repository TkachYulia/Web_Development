import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = range(a, b)
for i in x:
    if i%d == c:
        print (i)
