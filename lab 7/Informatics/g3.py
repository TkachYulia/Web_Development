import math
a = int(input())

x = range(2, a)
for i in x:
    if a%i == 0:
        print (i)
        break