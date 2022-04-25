## Nobel Prizes
In this exercise, you'll create a program to query a collection of Nobel prize winners by year or by category.

Concretely, you'll write two functions. First, you'll have to write

def load_nobel_prizes(filename='prize.json'):
    return {}
Then, you'll have to fill out the rest of

def main(year, category):
    data = load_nobel_prizes()
    ...
This program will print out information about Nobel prizes (in any format you'd like). If a year is specified (not None), only print information about Nobel prizes from that year. If a category is specified (not None), only print information about Nobel prizes from that category.

This program is executed at the command line with arguments determined by a parser we wrote in the helper module.

So, you can run

$ python3 nobel.py
...
$ python3 nobel.py --year 2020
...
$ python3 nobel.py --category Physics
...
$ python3 nobel.py --year 1901 --category Economics
...
The command-line arguments are the values passed to your main function.