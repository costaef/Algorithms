t = int(raw_input()) # number of test cases

for i in range(t):
    line1 = raw_input().split()
    line2 = raw_input().split()

    n = int(line1[0]) # total students
    k = int(line1[1]) # minimun students required in class
    arrival_times = [int(x) for x in line2] # arrival times of each student

    students_in_class = 0
    for j in arrival_times:
        if j <= 0:
            students_in_class += 1
        
    if students_in_class >= k:
        print 'NO'
    else:
        print 'YES'
