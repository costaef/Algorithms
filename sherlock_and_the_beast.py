def max_5(digits):
    w_5 = digits / 3
    left = digits - (w_5 * 3)
    if left > 0:
        n = w_5
        for i in range(0,n):
            w_5 -= 1
            left = digits - (w_5 * 3)
            if left % 5 == 0:
                return w_5, left
        return -1, -1
    return w_5, 0

n_tests = int(raw_input())
for test in range(n_tests):
    digits = int(raw_input())

    if digits >= 3:
        weight_5, left_digits = max_5(digits)
        if weight_5 == -1:
            print -1
        else:
            print '5' * (weight_5 * 3) + '3' * left_digits
    else:
        print -1
