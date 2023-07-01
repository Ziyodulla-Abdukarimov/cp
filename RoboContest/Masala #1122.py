n = int(input())
if len(str(n)) % 2 != 0:
    t = True
    for i in str(n):
        if int(i) % 2 == 0:
            t = False
            break
    print("YES" if t else "NO")
else:
    print("NO")
