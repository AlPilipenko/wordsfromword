import json
from flask_word import word_list


with open(r"words_dictionary.json") as d:
    """Loads English dictionary (~61k words) with corresponding definitions"""
    word_list = json.load(d)


def word_builder(user_input: str) -> list:
    """
    Returns a list of words that can be made from the user input.
    """
    user_input_striped = user_input.replace(" ", "").lower()
    possible_words = []
    for word in word_list.keys():
        temp_user_input = user_input_striped
        contain_letters = True
        for letter in word:
            if letter not in temp_user_input:
                contain_letters = False
                break
            else:
                letter_index = temp_user_input.index(letter)
                temp_user_input = (temp_user_input[:letter_index]
                                             + temp_user_input[letter_index+1:])
        if contain_letters is True and len(word) > 1:
            possible_words.append(word)
    if user_input_striped in possible_words:
        possible_words.remove(user_input_striped)
    possible_words.sort(key=len)
    return possible_words


def possible_words_meaning(possible_words: list, max_description: int) -> dict:
    """Returns found words + meanings as a dictionary. The length of
    description is limited by max_description size.
    """
    temp_dictionary = {}
    for word in possible_words:

        description = word_list.get(word)
        description = description[:max_description]
        size = len(description)
        if size < 30 or description[-1] == "'" or description[-1] == '"':
            pass
        else:
            end = description.rfind(',')
            description = description[:end]
        description = description.replace('(', '')
        temp_dictionary[word] = description + '.'
    return temp_dictionary


def enum_and_group_words(words: list, n: int) -> list:
    """Enumerates words and split them in group of n-ths (10 - default)
    """
    enum_words = [f'{i}. {w}' for i, w in enumerate(words, 1)]
    grouped_words = [enum_words[i:i+n] for i in range(0, len(enum_words), n)]
    return grouped_words


def word_maker(user_input: str) -> dict:
    """
    Returns all possible words with corresponding definitions that can be
    made from the user input. Also, specifies the longest word and the total
    number of words.
    Preconditions:
    - input is a string.
    - maximum input length is 15 symbols when pictures disabled
    - maximum input length is 25 symbols when pictures enabled
    """
    possible_words = word_builder(user_input)
    total_words = len(possible_words)
    if total_words == 0:
        return {}
    temp_dictionary = possible_words_meaning(possible_words, 450)
    longest = [possible_words[-1], word_list.get(possible_words[-1])]
    possible_words = enum_and_group_words(possible_words, 10)
    word_data = {
                'total': total_words,
                'longest': longest,
                'possible_words': possible_words,
                'temp_dictionary': temp_dictionary
                }
    return word_data
