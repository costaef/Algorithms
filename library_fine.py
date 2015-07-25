line1 = raw_input().split()
line2 = raw_input().split()

actual_date = (int(line1[2]), int(line1[1]), int(line1[0]))
expected_date = (int(line2[2]), int(line2[1]), int(line2[0]))

if actual_date <= expected_date:
    print 0
else:
    if actual_date[0] == expected_date[0]:
        if actual_date[1] == expected_date[1]:
            print (actual_date[2] - expected_date[2]) * 15
        else:
            print (actual_date[1] - expected_date[1]) * 500
    else:
        print 10000
