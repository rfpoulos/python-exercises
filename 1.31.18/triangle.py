height = int(raw_input("How high would you like your triangle?: "))

for i in range(0, height + 1):
    print " " * (height - i) + "*" * (i * 2 - 1)