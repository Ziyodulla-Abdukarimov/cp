n = input()
k = 0
for i in n:
    if i != '9':
        n = n[:k] + '9' + n[k + 1:]
        break
    k += 1
print(n)
