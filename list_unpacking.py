numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
# this line is identical to lines 4-6 and called unpacking
first, *other, last = numbers

print(first, last)
print(other)

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
