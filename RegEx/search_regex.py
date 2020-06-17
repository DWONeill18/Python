import re

def regex(x):
    if x:
        print("YES! We have a match!")
    else:
        print("No match")

# Search regex
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned.


# Search the string to see if it starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
regex(x)

# Search for the first white-space character in the string
txt = "The rain in Spain"
x = re.search("\s", txt)
print(x.start())

# Returns no matches
x = re.search("Portugal", txt)
print(x)