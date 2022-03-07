"""Check whether a word is 'efficient' - if each letter can be drawn by a
pencil without lifting."""

EFFICIENT_LETTERS = set('BCDGIJLMNOPSUVWZ')


def is_efficient(letters):
    for letter in letters:
        if letter not in EFFICIENT_LETTERS:
            return False

    return True

result = is_efficient('PIMPLE')
print(result)


def swap_keys_and_values(d1):
    d2 = {}
    # d = {1: 'one', 2: 'two', 3: 'two'}
    print(d1.items())

    for key, value in d1.items():
        if value not in d2:
            d2[value] = set(str(key))
        else:
            d2.get(value).add(str(key))

    return d2


d = {'a': 1, 'b': 2, 'c': 1, 'd': 7}
print(swap_keys_and_values(d))