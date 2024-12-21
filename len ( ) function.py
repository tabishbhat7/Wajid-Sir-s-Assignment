def longest_word(words):
    longest = max(words, key=len)
    return (longest, len(longest))

result = longest_word(["tabish", "uman", "kamraan"])
print(result)