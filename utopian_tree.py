n_tests = int(raw_input())

for test in range(n_tests):
    n = int(raw_input())
    height = 1
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    print height
