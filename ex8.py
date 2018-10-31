# formatter is a string with space for our four variables
formatter = "{} {} {} {}"

# by calling formatter.format we can decide what variables to include in our string, even another strings which could be formatted again
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
