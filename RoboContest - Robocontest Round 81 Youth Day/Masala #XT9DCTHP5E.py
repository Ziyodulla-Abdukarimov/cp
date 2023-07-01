import math

N, R = map(int, input().split())
A, B, C = map(int, input().split())

points = 0
for _ in range(N):
    x, y = map(int, input().split())
    distance = math.sqrt(x**2 + y**2)  # Euclidean distance from the origin
    if distance <= R / 2:
        points += A
    elif distance <= R / 4:
        points += B
    elif distance <= R / 6:
        points += C

print(points)
