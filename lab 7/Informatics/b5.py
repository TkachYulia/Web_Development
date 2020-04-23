
n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
for i in a:
    if i % 2 == 0:
        print(i, end = ' ')