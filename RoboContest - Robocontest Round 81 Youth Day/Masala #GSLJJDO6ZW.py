N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

def count_subarrays(l, r):
    count = 0
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            if prefix_sum[j] - prefix_sum[i] == 0:
                count += 1
    return count

for _ in range(Q):
    L, R = map(int, input().split())
    result = count_subarrays(L, R)
    print(result)
