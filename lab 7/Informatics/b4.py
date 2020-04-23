import math
n = int(input())
i = 2
while i <= n:
    i = i+1
    if n%(i-1) == 0:
        print (i-1) 
        break


