s = input()
m = s.split(' ')
for i in m:
    if len(i) > 9:
        if len(i) % 2 == 0:
            d = len(i) // 2
            print(i[0: d], i[d:], sep='-', end='')
        else:
            d = len(i) // 2
            print(i[0:d], i[d:], sep='-', end='')
    else:
        print('-', i, sep='')
