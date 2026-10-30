text = input("Введите строку слов: ")

words = text.split()
unique_words = set(words)

print("Количество:", len(unique_words))
print("Слова:", " ".join(sorted(unique_words)))
