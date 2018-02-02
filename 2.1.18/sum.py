def sum_num(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

print sum_num([1, 2, 3, 4, 5])