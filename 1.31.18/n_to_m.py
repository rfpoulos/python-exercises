start = int(raw_input("Please enter starting number: "))
end = int(raw_input("Please enter ending number: "))

if end > start:
    for i in range(start, end + 1):
        print i
else:
    print "End must be higher than start."