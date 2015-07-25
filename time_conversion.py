time = raw_input().split(':')
hour = time[0]

if time[2].find('AM') != -1:
    if hour == '12':
        hour = '00'
else:
    if hour != '12':
        hour = str(12 + int(hour))
    
print '{0}:{1}:{2}'.format(hour, time[1], time[2][:2])
