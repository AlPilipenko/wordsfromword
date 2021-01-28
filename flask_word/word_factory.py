import json
from flask_word import word_list

with open(r"words_dictionary.json") as d:
    word_list = json.load(d)
    #print(len(word_list))


def words_building(word):
    "Trying to make words from dictionary with letters from the word given"
    word = str(word)
    word = word.replace(" ", "").lower()
    final_list = []

    for w in word_list.keys():
        if w == word:
            "Not including original word"
            continue

        test_word = word
        match = 0

        for l in w:
            try:
                d = test_word.index(l)
                test_word = test_word[:d] + test_word[(d+1):]
                match += 1
            except ValueError:
                continue

        if match == len(w) and len(w) > 1:
            final_list.append(w)

    final_list.sort(key=len)

    return final_list


def final_word_meaning(f_list, max_description):
    "To return found words + meanings"
    temp_dictionary = {}

    for w in f_list:

        v = word_list.get(w)
        v = v[:max_description]

        if len(v) < 30 or v[-1] == "'" or v[-1] == '"':
            pass
        else:
            while v[-1] != ',':
                v = v[:-1]
            v = v[:-1]
        v = v.replace('(', '')

        temp_dictionary[w] = v
    return temp_dictionary

def row_major(alist, n):
    "To return rows with n words"
    return [alist[i:i+n] for i in range(0, len(alist), n)]


def word_maker(given_word):
    "Main algo"
    final_list = words_building(given_word)

    "Prepearing to return key data"
    try:
        longest = [final_list[-1], word_list.get(final_list[-1])]
    except:
        longest = None #'Couldn"t find any words :('

    final_list.sort()

    "To return found words + meanings (max set 450 chars for description)"
    temp_dictionary = final_word_meaning(final_list, 450)

    "Enumerating words"
    final_list = [f'{i}. {w}' for i, w in enumerate(final_list,1)]


    "returning key data"
    total = len(set(final_list))
    final_list = row_major(final_list, 10)
    word_data = {
                'total' : total,
                'longest' : longest,
                'possible_words' : final_list,
                'temp_dictionary' : temp_dictionary
                }

    return word_data
