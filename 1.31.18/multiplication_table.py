input = int(raw_input("What size would you like your multiplication table?: "))

for i in range(1, input + 1):
    for j in range(1, input + 1):
        print "%s X %s = %s " % (i, j, i * j) 