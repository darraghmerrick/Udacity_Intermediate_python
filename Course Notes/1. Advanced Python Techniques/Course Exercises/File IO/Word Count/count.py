import collections


def count_unique_words(filename='hamlet.txt'):
    words = collections.Counter()
    # Extract the data into Python.
    with open(filename) as f:
        for line in f:
            words.update(line.split())

    # Calculate the ten most common words.
    for word, count in words.most_common(10):
        print(word, count)


if __name__ == '__main__':
    count_unique_words('hamlet.txt')