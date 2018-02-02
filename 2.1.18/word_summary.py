def histograham():
    words_or_letters = raw_input("Would you like to count word's or letters? (w / l): ")
    if words_or_letters == "w":
        user_input = raw_input("What word's would you like to count?: ")
        user_list = user_input.split(" ")
    else:
        user_input = raw_input("What word would you like to letter count?: ")
        user_list = list(user_input)

    letters_dict = {}
    for i in range(len(user_list)):
        if user_list[i] in letters_dict:
            letters_dict[user_list[i]] += 1
        else:
            letters_dict[user_list[i]] = 1
    print letters_dict

    dict_keys = letters_dict.keys()
    dict_values = letters_dict.values()
    list_tuples = []
    for i in range(len(dict_keys)):
        list_tuples.append((dict_keys[i], letters_dict[dict_keys[i]]))

    sorted_frequency = sorted(list_tuples, key=lambda occurance: occurance[1], reverse=True)
    print sorted_frequency
    print sorted_frequency[:3]

histograham()