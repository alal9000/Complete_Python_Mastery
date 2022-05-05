# second parameter is optional, if no argument is specified here in the function call then 1 will be used for by as default. When you explicitly state arg then it will be used instead
def increment(number, by=1):
    return number + by


print(increment(2, 5))
