# def fizz_buzz(input):
#     if input % 3 or 5 == 0:
#         return "fizz_buzz"
#     elif input % 3 == 0:
#         return "fizz"
#     elif input % 5 == 0:
#         return "buzz"
#     else:
#         return input


# print(fizz_buzz(15))


def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"

    return "Buzz"


print(fizz_buzz(15))
