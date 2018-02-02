def leetspeak(user_input):
 #   user_input = raw_input("What would you like to convert to leetspeak?: ")
    user_list = list(user_input)
    output = []
    for i in range(0, len(user_list)):
        if user_list[i] == "A" or user_list[i] == "a":
            output.append("4")
        elif user_list[i] == "E" or user_list[i] == "e":
            output.append("3")
        elif user_list[i] == "G" or user_list[i] == "g":
            output.append("6")
        elif user_list[i] == "I" or user_list[i] == "g":
            output.append("1")
        elif user_list[i] == "O" or user_list[i] == "o":
            output.append("0")
        elif user_list[i] == "S" or user_list[i] == "s":
            output.append("5")
        elif user_list[i] == "T" or user_list[i] == "t":
            output.append("7")
        else:
            output.append(user_list[i])

    return "".join(output)

print leetspeak(raw_input("What would you like to convert to leetspeak?: "))