n = int(input())
m = list(map(int, input().split()))

res = []
for i in range(101):
    if i in m:
        c = m.count(i)
        for j in range(c):
            res.append(i)
print(*res)

# Time Limit 8 Error
