import math
n = int(input())
i = 1
while i < n:
    d = int(math.sqrt(i))
    i = i+1
    if d*d == i-1:
        print (i-1)
        



