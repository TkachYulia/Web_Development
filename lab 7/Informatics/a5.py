n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
for i in range(0, n, 2):
    print(a[i], end = ' ')