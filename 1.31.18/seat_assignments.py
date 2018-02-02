yesterday_seat_assignments = [
    "Nick",
    "Chris",
    "Moses",
    "Jaehee",
    "Aaron",
    "Joel",
    "Ken",
    "Ashley"
]
today_seat_assignments = [
    "Nick",
    "Ashley",
    "Ken",
    "Joel",
    "Aaron",
    "Jaehee",
    "Blank",
    "Chris",
    "another example"
]
i = 0
seat_count = len(yesterday_seat_assignments)
while i < seat_count:
    if today_seat_assignments[i] == yesterday_seat_assignments[i]:
        print "Hey, %s can't sit here!" % today_seat_assignments[i]
    else:
        print "You can seat here."
    i += 1

print "We're done!"

for i in range(0, len(today_seat_assignments)):
    if today_seat_assignments[i] == yesterday_seat_assignments[i]:
        print "Hey, %s can't sit here!" % today_seat_assignments[i]
    else:
        print "You can seat here."
    

print "We're done!"

