import requests

from find_words_in_file import punctuation_remove

book = requests.get('https://www.gutenberg.org/cache/epub/345/pg345.txt')
lines = book.text.split('\n')
punctuation_remove = ",.!?;"
punctuation_space = "'\"()[]=-_"

for line in lines:
    for c in punctuation_remove:
        line = line.replace(c, "")
    for c in punctuation_space:
        line = line.replace(c, " ")
    words = line.split()
    for words in words:
        words = word.lower()
        unique_words[words] = unique_words.get(word, 0) + 1

    print(unique_words)