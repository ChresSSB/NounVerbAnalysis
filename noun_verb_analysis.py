from nltk.corpus import wordnet as wn


def load_wordnet_entries():
    """
    Loads all wordnet words
    :return: dictionary of all loaded words in a tuple, 0 index are words with nouns, verbs, and adjectives as keys
    1 index is counts with same keys as 0 index + total
    """

    # load all words in wordnet into lists and get the count
    nouns = [x.name().split('.', 1)[0] for x in wn.all_synsets('n')]
    nouns_count = len(nouns)

    verbs = [x.name().split('.', 1)[0] for x in wn.all_synsets('v')]
    verbs_count = len(verbs)

    adjectives = [x.name().split('.', 1)[0] for x in wn.all_synsets('a')]
    adjectives_count = len(adjectives)

    total_count = nouns_count + verbs_count + adjectives_count

    # format result
    word_dictionary = {"nouns": nouns, "verbs": verbs, "adjectives": adjectives}
    count_dictionary = {"nouns": nouns_count, "verbs": verbs_count, "adjectives": adjectives_count, "total": total_count}

    dictionary_result = (word_dictionary, count_dictionary)

    return dictionary_result


if __name__ == '__main__':
    dictionary = load_wordnet_entries()
    print(dictionary)

# print(nouns)
# print(verbs)
# print(adjs)

# main("design1")
# print("--------------")
# main("design2")
# print("--------------")
# main("Mini-MPACS")
# file = "design1"
# file = "design2"
# file = "design3"
# file = "Mini-MPACS"

