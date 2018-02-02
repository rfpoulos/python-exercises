bill = float(raw_input("What is the total bill? "))
service = raw_input("Level of service (good, fair, bad)? ")

if service == "good":
    tip = bill * 0.2
    total = bill + tip
elif service == "fair":
    tip = bill * 0.15
    total = bill + tip
elif service == "bad":
    tip = bill * 0.1
    total = bill + tip

print 'The tip is $%.2f, the total is $%.2f' % (tip, total) 

split = raw_input("Would you like to split the bill (y/n)? ")

if split == "y":
    split_people = int(raw_input("How many people?" ))
    per_person = total / split_people
    per_person_tip = tip / split_people
    print "The tip per person is: $%.2f" % per_person_tip
    print "Total per person is: $%.2f" % per_person