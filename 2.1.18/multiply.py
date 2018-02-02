def multiply(a, b):
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i] * b)
    return new_list

print multiply([1, 2, 3, 4, 5], 5)
