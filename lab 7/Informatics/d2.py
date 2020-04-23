import math
 
a = int(input())
x = math.copysign(1, a)
if(a == 0): x =0
print (int(x))