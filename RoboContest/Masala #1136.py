i = input()
w = i.split(" ")
o = []
for a in w:
    if len(a) >= 10:
        f = a[:int(len(a) / 2)]
        s = a[int(len(a) / 2):]
        o.append(f + "-" + s)
    else:
        o.append(a)
t = "-".join(o)
print(t)
