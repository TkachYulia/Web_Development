n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
cnt = 0
for i in a:
    if i > 0:
        cnt+=1
print(cnt)