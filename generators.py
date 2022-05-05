from sys import getsizeof


values = (x * 2 for x in range(100000))
# for x in values:
#     print(x)


# # print(values)

# print("Gen:", getsizeof(values))


# values = [x * 2 for x in range(100000)]
# print("List:", getsizeof(values))

print(len(values))
