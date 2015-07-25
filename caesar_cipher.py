def lower_rotate(char, n):
    count = ord(char)
    for i in range(0, n):
        count = count + 1
        if count > 122:
            count = 97
    return count

def upper_rotate(char, n):
    count = ord(char)
    for i in range(0, n):
        count = count + 1
        if count > 90:
            count = 65
    return count

n = int(raw_input())
message = raw_input()
k = int(raw_input())

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher = ''

for i in range(n):
    char = message[i]
    if char in lowercase_letters:
        cipher = cipher + chr(lower_rotate(char, k))
    elif char in uppercase_letters:
        cipher = cipher + chr(upper_rotate(char, k))
    else:
        cipher = cipher + char

print cipher
