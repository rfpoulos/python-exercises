user_input = raw_input("What would you like to reverse?: ")
split_input = list(user_input)
character_len = len(split_input)
reverse_string = []
for i in range(0, character_len):
    reverse_string.append(split_input[character_len - i - 1])
print "".join(reverse_string)