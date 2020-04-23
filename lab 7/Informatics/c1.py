import math
num1 = int(input())
num2 = int(input())
a=abs(num1)*num2
ans = 0
def cnt(a):
if a > 108:
    a-108
    cnt()
    else:
        ans = a

cnt()
print (ans)