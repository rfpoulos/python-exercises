input = int(raw_input("What number would you like to factor?: "))
for i in range(1, input +1):
    if input % i == 0:
        print i