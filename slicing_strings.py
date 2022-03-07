
hello = 'Hello, world!'
a = hello[0]
b = hello[-2]
c = hello[1:5]
d = hello[-6:]
e = hello[::2]
f = hello[::-1]

#print(a)

def make_palindrome(s):
    return s + s[::-1] 


print(make_palindrome("helloWorld"))


def add_layer(triangle):
    last = triangle[-1]  # The most recent row of Pascal's triangle.
    row = []  # Build up the next row.
    for left, right in zip(last + (0,), (0,) + last):
        row.append(left + right)
    triangle.append(tuple(row))
