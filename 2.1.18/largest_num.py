def largest(numbers):
    list_numbers = sorted(numbers, reverse=True)
    return list_numbers[0]

print largest([1, 2, 3, 5, 4])