def find_number(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1

print(find_number([10, 25, 30, 45], 30))
print(find_number([5, 8, 5, 9], 5))
print(find_number([10, 30, 30], 99))
