# findall() function returns a list containing all matches

import re

def regex(x):
    if x:
        print("YES! We have a match!")
    else:
        print("No match")

# Finds all instances of "ai" and prints them in a list
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# If none are found, an empty list is printed instead
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# \b Returns a match where the specified characters are at the beginning or at the end of a word

txt_b3 = "ain't it quaint"
txt_b4 = "The rain in Spain"

b3 = re.findall(r"\bain", txt_b3)
b4 = re.findall(r"ain\b", txt_b4)
print(b3)
print(b4)

regex(b3)
regex(b4)

# \Z Returns a match if the specified characters are at the end of the string

txt_b5 = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt_b5)
print(x)

