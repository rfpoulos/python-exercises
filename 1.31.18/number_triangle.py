input = int(raw_input("How many numbers would you like to triangle?: "))
for i in range(0, input + 1):
    print "%s triangled = %s" % (i, (i * (i + 1)) / 2)