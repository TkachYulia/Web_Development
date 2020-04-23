
n = int(input())

if (n % 2 != 0) | ((n % 2 == 0) & (n in range(6, 20))):
    print("Weird")

elif ((n % 2 == 0) & (n in range(2, 5))) | ((n % 2 == 0) & (n > 20)):
    print("Not Weird")