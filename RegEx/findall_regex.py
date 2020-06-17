# findall() function returns a list containing all matches

import re

# Finds all instances of "ai" and prints them in a list
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# If none are found, an empty list is printed instead
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
