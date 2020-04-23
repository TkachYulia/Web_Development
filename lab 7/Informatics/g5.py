n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
for i in range(len(a)//2):
    a[n-i-1], a[i] = a[i], a[n-i-1]
for i in a:
    print(i, end = ' ')