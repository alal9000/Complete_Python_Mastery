items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]    # same as above but shorter and cleaner
print(prices)

# filtered = list(filter(lambda item: item[1] >= 10, items))
# same as above but shorter & cleaner
filtered = [item for item in items if item[1] >= 10]
print(filtered)


print(items[2])
