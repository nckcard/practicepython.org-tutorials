word = input("Input a word: ")

#wordlen = len(word)
#
#for i in range(wordlen):
#  if word[i] == word[wordlen-i-1]:
#    palindrome = True
#  else:
#    palindrome = False
#    break

revword = word[::-1]

if word == revword:
  palindrome = True
else:
  palindrome = False

if palindrome:
  print(word + " is a palindrome!")
else:
  print(word + " is NOT a palindrome.")
