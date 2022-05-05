def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number  # augmented assignment operator
    return total


print(multiply(2, 3, 4, 5))
