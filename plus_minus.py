n = int(raw_input())
positives = 0
zeros = 0
negatives = 0

line = raw_input().split()
numbers = [int(s) for s in line]

for i in range(n):
    if numbers[i] > 0:
        positives = positives + 1
    elif numbers[i] < 0:
        negatives = negatives + 1
    else:
        zeros = zeros + 1

print "{0:.3f}".format(float(positives) / n)
print "{0:.3f}".format(float(negatives) / n)
print "{0:.3f}".format(float(zeros) / n)
