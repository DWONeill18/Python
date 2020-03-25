# python tricks

# function to comment if a number is even
def is_even(x):
    if x %2 == 0:
        return True
    else:
        return False

print(is_even(900))

# We’ll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0
def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False

# Test an integer without using type()
from math import *
def is_int(x):
    if floor(x)-x==0: #here you can use “ceil” instead of "floor"
        return True
    else:
        return False

print(is_int(6))
print(is_int(6.5))
#print(is_int(hello))

# Add the digits of a number to calculate the sum
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print(x)
    return total

print(digit_sum(1234))

# Calcukate tghe factoruial of a non negative integer
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total

print(factorial(5))

# Testing for a prime number
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print(is_prime(17))

# Reverse a string
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print(reverse("Hello World"))

# remove vowels from string
def anti_vowel(text):
  word = ""
  for char in text:
    if char not in "aeiouAEIOU":
      word += char
  return word

print(anti_vowel("HeLlO hOw ArE yOu?"))

# scrabble
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    word = word.lower()
    total = 0
    for char in word:
        total = total + score[char]
    return total

print(scrabble_score("abc"))

# censor a word in a sentence
def censor(text, word):
    # split the string so you can loop through it
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    # loop through the indices in the list and replace words with stars
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print(censor("what the beep is going on!!", "beep"))

# count the number of times an item appear in a list
def count(sequence, item):
  count = 0
  for x in sequence:
    if x == item:
      count += 1
  return count

print(count([1, 1, 2, 3, 5, 5, 6, 7, 7, 7, 8], 7))

# purify will remove odd numbers from a list
def purify(sequence):
  second_seq = []
  for num in sequence:
    if num % 2 == 0:
      second_seq.append(num)
  return second_seq

print(purify([1, 2, 3, 4]))

# product will give the product of all numbers in the list
def product(lst):
  total = 1
  for ele in lst:
    total *= ele
  return total

print(product([1, 2, 3, 4]))

# removes duplicates from a list
def remove_duplicates(inputlist):
    if inputlist == []:
        return []    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # append values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
  
print(remove_duplicates([1, 1, 2, 2]))


# sort a list then calculate a the median value,
# if an even number of items in list then calculate the mean of the two middle items
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd no. of elements
        #//2 give floor division = middle index
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        #/ give float so need // for integer indices
        index_1 = len(sorted_list)//2 -1
        #print(index_1)
        index_2 = len(sorted_list)//2
        #print(index_2)
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print(median([2, 4, 5, 9]))