sentence = input("Write a sentence: ")

words = sentence.split()

words_rev = words[::-1]

sentence_rev = " ".join(words_rev)

print(sentence_rev)


# one line solution:
def reverseWord(w):
  return ' '.join(w.split()[::-1])
