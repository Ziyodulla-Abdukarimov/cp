N = int(input())

def find_char_at_position(N):
    position = (N - 1) % 26
    char = chr(ord('a') + position)
    return char

result = find_char_at_position(N)
print(result)
