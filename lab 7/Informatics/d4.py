n = int(input())
i = 0
x = True
while n != 0:
    
    if n%2 == 0:
        n = n/2
    else:
    x = False
    break

if x == False:
    print ("NO")
    else:
    print ("YES")
