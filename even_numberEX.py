

# number = range(1, 10)

# for x in number:
#     if x
#         print(x)


# print("We have 4 even numbers")

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"There are {count} numbers")
