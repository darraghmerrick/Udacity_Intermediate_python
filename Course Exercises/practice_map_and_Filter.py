# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

def reverse(s):
    return s[::-1]

def first_two(s):
    return s[:2]

a = map(len, ["apple", "orange", "pear"])
b = map(str.upper, ["apple", "orange", "pear"])
c = map(reverse, ["apple", "orange", "pear"])  # Could also be with a lambda function.
d = map(first_two, ["apple", "orange", "pear"])  # Could also be with a lambda function.


# Practice with filter
# Fill out the rest of the filter functions.
# You can define additional functions if you need to.
# (a) range(100) => (0, 3, 6, 9, ...)  (div by 3)
# (b) range(100) => (0, 5, 10, 15, ...)  (div by 5)
# (c) range(100) => (0, 15, 30, 45, ...)  (div by 15)
# (d) range(100) => (1, 2, 4, 7, 8, 11, 13, 14)  (not div by 3 and not div by 5)

a = filter(lambda x: x % 3 == 0, range(100))
b = filter(lambda x: x % 5 == 0, range(100))
c = filter(lambda x: x % 15 == 0, range(100))
d = filter(lambda x: x % 3 != 0 and x % 5 != 0, range(100))