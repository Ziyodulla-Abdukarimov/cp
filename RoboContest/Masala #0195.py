n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
s = 0
for i in range(len(m) - 1):
    s += m[i] ^ m[i + 1]
print(s)
