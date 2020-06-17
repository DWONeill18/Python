# The sub() function replaces the matches with the text of your choice

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)