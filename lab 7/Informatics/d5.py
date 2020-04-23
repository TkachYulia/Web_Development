n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
cnt = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        cnt+=1

print(cnt)