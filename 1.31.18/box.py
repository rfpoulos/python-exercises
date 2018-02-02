width = int(raw_input("How many units wide would you like your rectangle?: "))
height = int(raw_input("How high would you like your rectangle?: "))

print "*" * width
for i in range(0, height - 2):
    print "*" + " " * (width - 2) + "*"
print "*" * width