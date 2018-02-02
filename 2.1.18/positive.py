def positive(numbers):
    positive_list = []
    for i in range(len(numbers)):
        if numbers[i] > 0:
            positive_list.append(numbers[i])
    return positive_list

print positive([-1, 2, -3, 4])