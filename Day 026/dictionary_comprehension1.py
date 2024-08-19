sentence = (input("Write a sentence: ")).split()

result = {word: len(word) for word in sentence}
print(result)
