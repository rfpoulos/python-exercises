def vectors(a, b):
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i] * b[i])
    return new_list

print vectors([1, 2, 3], [1, 2, 3])