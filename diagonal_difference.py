n = int(raw_input())
first_diagonal_sum = 0
second_diagonal_sum = 0

for i in range(n):
    line = raw_input().split()
    first_diagonal_sum = first_diagonal_sum + int(line[i])
    second_diagonal_sum = second_diagonal_sum + int(line[n-1-i])

difference = abs(first_diagonal_sum - second_diagonal_sum)

print difference
