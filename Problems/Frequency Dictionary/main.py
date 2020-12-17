words = input().lower().split(" ")

words_count = {}

for word in words:
    words_count[word] = words.count(word)

for key in words_count:
    print(key, words_count[key])
