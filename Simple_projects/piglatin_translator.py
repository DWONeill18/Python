# Pig Latin translator (python 3 - raw_input and print different syntax from py2)

pyg = 'ay'

# Take an input from user
original = input('Enter a word:')

# Check if a value has been inputted and is just made of letters, otherwise prints 'empty'
if len(original) > 0 and original.isalpha():
    # Make word lowercase, take first letter of the word and 'ay', add them to the end of the word
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    print (new_word)
    # The new word is the old word with the first letter taken away, added to the end with 'ay' appended
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print ('empty')