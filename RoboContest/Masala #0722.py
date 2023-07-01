def find_largest_xor(N):
    if N == 0:
        return 0
    msb_position = 0
    temp = N
    while temp != 0:
        temp = temp >> 1
        msb_position += 1
    largest_xor = (1 << msb_position) - 1
    return largest_xor



N = int(input())
largest_xor = find_largest_xor(N)
print(largest_xor)
