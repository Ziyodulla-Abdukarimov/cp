def is_triangular_number(number):
    n = 0
    triangular = 0

    while triangular < number:
        n += 1
        triangular = (n * (n + 1)) // 2

    return triangular == number


n = int(input())
m = list(map(int, input().split()))
for i in m:
    if is_triangular_number(i):
        print(1, end='')
    else:
        print(0, end='')
