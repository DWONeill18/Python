# RegEx - Regular Expressions searching for sequences within text
import re

def regex(x):
    if x:
        print("YES! We have a match!")
    else:
        print("No match")

#Literals

# matching bark but NOT baa, bellow, boom
txt_a = "bark"
a = re.search("bark", txt_a)
#regex(a)

#Alternation

# matching cat or dog
txt_b = "cat"
txt_c = "dog"
b = re.search("cat|dog", txt_b)
c = re.search("cat|dog", txt_c)
#regex(b)
#regex(c)

#Character Sets

# matching cat, hat or rat but NOT eat, mat, sat
txt_d = "cat"
txt_e = "hat"
txt_f = "rat"
txt_g = "eat"
txt_h= "mat"
txt_i = "sat"
d = re.search("[chr]at", txt_d)
e = re.search("[chr]at", txt_e)
f = re.search("[chr]at", txt_f)
g = re.search("[chr]at", txt_g)
h = re.search("[chr]at", txt_h)
i = re.search("[chr]at", txt_i)
#regex(d)
#regex(e)
#regex(f)
#regex(g)
#regex(h)
#regex(i)

#Wildcards

# matching bear., lion., orca. but NOT mouse, koala, snail
txt_j = "bear."
txt_k = "lion."
txt_l = "orca."
txt_m = "mouse"
txt_n= "koala"
txt_o = "snail"
j = re.search("....\.", txt_j)
k = re.search("....\.", txt_k)
l = re.search("....\.", txt_l)
m = re.search("....\.", txt_m)
n = re.search("....\.", txt_n)
o = re.search("....\.", txt_o)
#regex(j)
#regex(k)
#regex(l)
#regex(m)
#regex(n)
#regex(o)

#Ranges

# matching cub, dog, elk but NOT ape, cow, ewe
txt_p = "cub"
txt_q = "dog"
txt_r = "elk"
txt_s = "ape"
txt_t= "cow"
txt_u = "ewe"
p = re.search("[c-e][uol][bgk]", txt_p)
q = re.search("[c-e][uol][bgk]", txt_q)
r = re.search("[c-e][uol][bgk]", txt_r)
s = re.search("[c-e][uol][bgk]", txt_s)
t = re.search("[c-e][uol][bgk]", txt_t)
u = re.search("[c-e][uol][bgk]", txt_u)
#regex(p)
#regex(q)
#regex(r)
#regex(s)
#regex(t)
#regex(u)

#Shorthand Character Classes ( \w, \d, \s, \W, \D, \S )

#matching "5 sloths", "8 llamas", "7 hyenas" but NOT "one bird", "two owls"
#regex \d\s\w\w\w\w\ws
#regex \d\s\w\w\w\w\w\w

#Grouping

#matching "puppies are my favorite!", "kitty cats are my favorite!" and NOT
# "deer are my favorite!", "otters are my favorite!", "hedgehogs are my favorite!"
#regex (puppies|kitty cats) are my favorite!

#Quantifiers Fixed

#matching "squeaaak", "squeaaaak", "squeaaaaak" but NOT
# "squeak", "squeaak", "squeaaaaaak"

#regex squea(3,5)k

#Quantifiers Optional

#matching "1 duck for adoption?", "5 ducks for adoption?", "7 ducks for adoption?"
#regex \d\sducks?\sfor\sadoption\?

#Quantifiers - 0 or more, 1 or more - Kleene

#matching "hoot", "hoooooot", "hooooooooooot" but NOT
# "hot", "hoat", "hoo"

#regex hoo+t
#regex hoo*t matches "hot" as well 

#Anchors

#matching "penguins are cooler than regular expressions" but NOT
# "king penguins are cooler than regular expressions", "penguins are cooler than regular expressions!"
#regex ^penguins\sare\scooler\sthan\sregular\sexpressions$