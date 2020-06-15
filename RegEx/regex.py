# RegEx - Regular Expressions searching for sequences within text
import re

#Literals

# matching bark but NOT baa, bellow, boom
regex bark

#Alternation

# matching cat or dog
regex cat|dog

#Character Sets

# matching cat, hat or rat but NOT eat, mat, sat
regex [chr]at

#Wildcards

# matching bear., lion., orca. but NOT mouse, koala, snail
regex ....\.

#Ranges

# matching cub, dog, elk but NOT ape, cow, ewe
regex [c-e][uol][bdk]

#Shorthand Character Classes ( \w, \d, \s, \W, \D, \S )

#matching "5 sloths", "8 llamas", "7 hyenas" but NOT "one bird", "two owls"
regex \d\s\w\w\w\w\ws
regex \d\s\w\w\w\w\w\w

#Grouping

#matching "puppies are my favorite!", "kitty cats are my favorite!" and NOT
# "deer are my favorite!", "otters are my favorite!", "hedgehogs are my favorite!"
regex (puppies|kitty cats) are my favorite!

#Quantifiers Fixed

#matching "squeaaak", "squeaaaak", "squeaaaaak" but NOT
# "squeak", "squeaak", "squeaaaaaak"

regex squea(3,5)k

#Quantifiers Optional

#matching "1 duck for adoption?", "5 ducks for adoption?", "7 ducks for adoption?"
regex \d\sducks?\sfor\sadoption\?

#Quantifiers - 0 or more, 1 or more - Kleene

#matching "hoot", "hoooooot", "hooooooooooot" but NOT
# "hot", "hoat", "hoo"

regex hoo+t
#regex hoo*t matches "hot" as well 

#Anchors

#matching "penguins are cooler than regular expressions" but NOT
# "king penguins are cooler than regular expressions", "penguins are cooler than regular expressions!"
regex ^penguins\sare\scooler\sthan\sregular\sexpressions$