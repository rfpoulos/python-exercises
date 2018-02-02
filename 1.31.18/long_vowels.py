user_input = raw_input("What would you like to extend?: ")
input_list = list(user_input)

output = []
vowel_count = 0

for i in range(0, len(input_list)):
    if input_list[i] == "a" or input_list[i] == "e" or input_list[i] == "i" or input_list[i] == "o" or input_list == "y":
        vowel_count += 1
        if vowel_count == 2:
            output.append(input_list[i] * 3)
    output.append(input_list[i])

print "".join(output)