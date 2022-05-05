browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])


if not browsing_session:  # if list is not empty
    browsing_session[-1]  # get item on top of the stack


# falsy values
0
""
not []
