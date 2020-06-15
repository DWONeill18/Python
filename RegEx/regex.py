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




