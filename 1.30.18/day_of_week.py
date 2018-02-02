day_int = int(raw_input('Enter a number 1-7: '))

if day_int == 1:
    day = "Sunday"
elif day_int == 2:
    day = "Monday"
elif day_int == 3:
    day = "Tuesday"
elif day_int == 4:
    day = "Wednesday"
elif day_int == 5:
    day = "Thursday"
elif day_int == 6:
    day = "Friday"
elif day_int == 7:
    day = "Saturday"
else:
    print "Invalid input"

print day

if day_int >= 2 and day_int <= 6:
    print "Go to work!"
elif day_int == 1 or  day_int == 7:
    print "Sleep in!"