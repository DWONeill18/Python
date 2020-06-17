# split() function returns a list where the string has been split at each match

import re

# Split at each whitespace

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# You can control the number of occurances by specifying the maxsplit parameter

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)