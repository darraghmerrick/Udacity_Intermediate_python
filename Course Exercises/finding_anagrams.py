from wordsets import english_words, english_words_small

# ADD YOUR CODE BELOW


def count_letters(letters):
    # store the count of each letter in the letters variable
    letters_dict = {}

    for char in letters:
        if char not in letters_dict:
            letters_dict[char] = letters.count(char)

    return letters_dict


def find_anagrams(letters, words):
    result_set = set()

    for word in words:
        if len(letters) != len(word):
            # next word
            continue
        else:
            # get a dict of letter: count values for letters
            letters_dict = count_letters(letters)
            for key, value in letters_dict.items():
                if key in word and value == word.count(key):
                    result_set.add(word)

    return result_set


# ADD YOUR CODE BELOW

if __name__ == '__main__':
    while True:
        letters1 = input(
            "What letters would you like "
            "to find the anagram of? ").lower().strip()
        for anagram in find_anagrams(letters1, english_words_small):
            print(anagram)