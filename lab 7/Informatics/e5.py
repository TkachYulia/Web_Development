n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
cnt = 0
for i in range(1, n):
    if ((a[i] > 0) & (a[i - 1] > 0)) | ((a[i] < 0) & (a[i - 1] < 0)):
        cnt = 1
        break
if cnt == 1:
    print('YES')
else:
    print('NO')