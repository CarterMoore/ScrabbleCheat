values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
          'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
          'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
          'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

words_values = {}


def check_match(letters, word):
    usable_letters = list(letters)
    try:
        for letter in word:
            usable_letters.remove(letter)
    except ValueError:
        return False
    else:
        return True


def get_value(word):
    score = 0
    for letter in word:
        score += values[letter]
    words_values[word] = score


def search_word(letters):
    with open('words.txt', 'r') as file:
        all_words = file.read().split('\n')

        for word in all_words:
            if check_match(letters, word):
                get_value(word)


if __name__ == '__main__':
    letters = input('Enter letters: ').lower()
    search_word(letters)
    print(words_values)
