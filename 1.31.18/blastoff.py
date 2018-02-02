import time
numbers = int(raw_input("How many numbers should we count down?: "))
text = raw_input("What should we say when we finish out countdown?: ")

for i in range(0, numbers + 1):
    if numbers - i == 0:
        print text
    else:
        print numbers - i
        time.sleep(1)
