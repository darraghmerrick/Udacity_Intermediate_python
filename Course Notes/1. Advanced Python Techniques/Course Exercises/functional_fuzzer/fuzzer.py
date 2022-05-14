import helper

def generate_cases():
    size = 0
    while True:
        yield helper.random_list(size)
        size += 1

'''
Solution 2
import itertools
import helper

def generate_cases_another_alternative():
    return map(helper.random_list, itertools.count())
'''

'''
Solution 3

import itertools
import helper

def generate_cases_alternative():
    return (helper.random_list(size) for size in itertools.count())

'''