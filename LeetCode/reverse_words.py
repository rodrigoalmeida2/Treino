def reverseWords(s: str) -> str:
    words = s.split(" ")
    print(words)
    reversed_words = []

    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        reversed_words.append(reversed_word)

    return " ".join(reversed_words)


print(reverseWords("the sky is blue"))
# Mais rápido: return ' '.join(word[::-1] for word in s.split())