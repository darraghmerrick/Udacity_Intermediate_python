
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


# Manipulating Lists and Tuples
# Write a function to produce the next layer of Pascal's triangle
# Each layer is one larger than the previous layer, and each element in
# the new layer is the sum of the two elements above it in the previous
# layer. For example, `(1, 3, 3, 1) -> (1, 4, 6, 4, 1)`.
#
# Hint: What does the expression `zip(row + (0,), (0,) + row)` produce?

def add_layer(triangle):
    last = triangle[-1]  # The most recent row of Pascal's triangle.
    row = []  # Build up the next row.
    for left, right in zip(last + (0,), (0,) + last):
        row.append(left + right)
    triangle.append(tuple(row))
    print(triangle)
    
    
pascals_triangle = [
    (1,),
    (1, 1),
    (1, 2, 1),
    (1, 3, 3, 1),
]

# Add a few layers, just to check.
for _ in range(5):
    add_layer(pascals_triangle)


