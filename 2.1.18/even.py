def even(numbers):
    even_list = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_list.append(numbers[i])
    return even_list

print even([1, 2, 3, 4, 5, 6, 7, 8])
