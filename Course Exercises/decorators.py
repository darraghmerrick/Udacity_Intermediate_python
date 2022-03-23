#Example 1
print("Example 1")
def perform_twice(fn, *args, **kwargs):
    fn(*args, **kwargs)
    fn(*args, **kwargs)

perform_twice(print, 5, 10, sep='&', end='...')

# Example 2
print("\nExample 2")
def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n

div_by_3 = make_divisibility_test(3)
tuple(filter(div_by_3, range(10)))  # => (0, 3, 6, 9)

make_divisibility_test(5)(10)  # => True

# Example 3 
print("\nExample 3")
def print_args(function):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)
    return wrapper

def compute(x, y, z=1):
    return (x + y) * z

compute(3, 5, z=2)
# => 16

compute_log = print_args(compute)
compute_log(3, 5, z=2)
# (3, 5) {'z': 2}
# => 16

compute = print_args(compute)
compute(3, 5, z=2)
# (3, 5) {'z': 2}
# => 16