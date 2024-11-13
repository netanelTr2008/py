def most_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    words_milon = {}

    for word in words:
        if word in words_milon:
            words_milon[word] += 1
        else:
            words_milon[word] = 1

    common_word = None
    max_count = 0

    for word, count in words_milon.items():
        if count > max_count:
            max_count = count
            common_word = word

    return common_word, max_count

file = "text.txt"
common_word, count = most_words(file)

print(f"the most common word is '{common_word}', it appears '{count}' times.")
def most_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    words_milon = {}

    for word in words:
        if word in words_milon:
            words_milon[word] += 1
        else:
            words_milon[word] = 1

    common_word = None
    max_count = 0

    for word, count in words_milon.items():
        if count > max_count:
            max_count = count
            common_word = word

    return common_word, max_count

file = "textt.txt"
common_word, count = most_words(file)

print(f"the most common word is '{common_word}', it appears '{count}' times.")