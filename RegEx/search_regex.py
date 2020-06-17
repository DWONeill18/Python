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

# The Match object has other proprties and methods used to retrieve information about the search and the result

# The .span() method returns a tuple containing the start and end postions of the match

# Searches words with an uppercase S
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# The .string() method returns the string passed into the function

# Prints the string passed into the function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# The .group() method returns the part of the string where there was a match
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
