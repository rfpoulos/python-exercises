def de_dup(things):
    new_list = []
    for thing in things:
        if thing not in new_list:
            new_list.append(thing)
    return new_list

print de_dup(["a", "b", "c", "d", "c", "d", "e", "f", "g"])