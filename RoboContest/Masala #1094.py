n = int(input())
m = [*range(1, n + 1)]
n = []
for i in m:
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        n.append(i)
print(sum(n))
