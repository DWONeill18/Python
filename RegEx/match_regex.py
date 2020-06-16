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
a = re.match("bark", txt_a)
#regex(a)

#Alternation

# matching cat or dog
txt_b = "cat"
txt_c = "dog"
b = re.match("cat|dog", txt_b)
c = re.match("cat|dog", txt_c)
"""
regex(b)
regex(c)
"""

#Character Sets

# matching cat, hat or rat but NOT eat, mat, sat
txt_d = "cat"
txt_e = "hat"
txt_f = "rat"
txt_g = "eat"
txt_h= "mat"
txt_i = "sat"

d = re.match("[chr]at", txt_d)
e = re.match("[chr]at", txt_e)
f = re.match("[chr]at", txt_f)
g = re.match("[chr]at", txt_g)
h = re.match("[chr]at", txt_h)
i = re.match("[chr]at", txt_i)

"""
regex(d)
regex(e)
regex(f)
regex(g)
regex(h)
regex(i)
"""

#Wildcards

# matching bear., lion., orca. but NOT mouse, koala, snail
txt_j = "bear."
txt_k = "lion."
txt_l = "orca."
txt_m = "mouse"
txt_n= "koala"
txt_o = "snail"

j = re.match("....\.", txt_j)
k = re.match("....\.", txt_k)
l = re.match("....\.", txt_l)
m = re.match("....\.", txt_m)
n = re.match("....\.", txt_n)
o = re.match("....\.", txt_o)

"""
regex(j)
regex(k)
regex(l)
regex(m)
regex(n)
regex(o)
"""

#Ranges

# matching cub, dog, elk but NOT ape, cow, ewe
txt_p = "cub"
txt_q = "dog"
txt_r = "elk"
txt_s = "ape"
txt_t= "cow"
txt_u = "ewe"

p = re.match("[c-e][uol][bgk]", txt_p)
q = re.match("[c-e][uol][bgk]", txt_q)
r = re.match("[c-e][uol][bgk]", txt_r)
s = re.match("[c-e][uol][bgk]", txt_s)
t = re.match("[c-e][uol][bgk]", txt_t)
u = re.match("[c-e][uol][bgk]", txt_u)

"""
regex(p)
regex(q)
regex(r)
regex(s)
regex(t)
regex(u)
"""

#Shorthand Character Classes ( \w, \d, \s, \W, \D, \S )

#matching "5 sloths", "8 llamas", "7 hyenas" but NOT "one bird", "two owls"
#regex \d\s\w\w\w\w\ws
#regex \d\s\w\w\w\w\w\w

txt_v = "5 sloths"
txt_w = "8 llamas"
txt_x = "7 hyenas"
txt_y = "one bird"
txt_z= "two owls"

v = re.match("\d\s\w\w\w\w\w\w", txt_v)
w = re.match("\d\s\w\w\w\w\w\w", txt_w)
x = re.match("\d\s\w\w\w\w\w\w", txt_x)
y = re.match("\d\s\w\w\w\w\w\w", txt_y)
z = re.match("\d\s\w\w\w\w\w\w", txt_z)

"""
regex(v)
regex(w)
regex(x)
regex(y)
regex(z)
"""

#Grouping

#matching "puppies are my favorite!", "kitty cats are my favorite!" and NOT
# "deer are my favorite!", "otters are my favorite!", "hedgehogs are my favorite!"
#regex (puppies|kitty cats) are my favorite!

txt_aa = "puppies are my favorite!"
txt_ab = "kitty cats are my favorite!"
txt_ac = "deer are my favorite!"
txt_ad = "otters are my favorite!"
txt_ae= "hedgehogs are my favorite!"

aa = re.match("(puppies|kitty cats) are my favorite!", txt_aa)
ab = re.match("(puppies|kitty cats) are my favorite!", txt_ab)
ac = re.match("(puppies|kitty cats) are my favorite!", txt_ac)
ad = re.match("(puppies|kitty cats) are my favorite!", txt_ad)
ae = re.match("(puppies|kitty cats) are my favorite!", txt_ae)

"""
regex(aa)
regex(ab)
regex(ac)
regex(ad)
regex(ae)
"""

#Quantifiers Fixed

#matching "squeaaak", "squeaaaak", "squeaaaaak" but NOT
# "squeak", "squeaak", "squeaaaaaak"
#regex squea{3,5}k

txt_af = "squeaaak"
txt_ag = "squeaaaak"
txt_ah = "squeaaaaak"
txt_ai = "squeak"
txt_aj = "squeaak"
txt_ak = "squeaaaaaak"

af = re.match("squea{3,5}k", txt_af)
ag = re.match("squea{3,5}k", txt_ag)
ah = re.match("squea{3,5}k", txt_ah)
ai = re.match("squea{3,5}k", txt_ai)
aj = re.match("squea{3,5}k", txt_aj)
ak = re.match("squea(3,5)k", txt_ak)

"""
regex(af)
regex(ag)
regex(ah)
regex(ai)
regex(aj)
regex(ak)
"""

#Quantifiers Optional

#matching "1 duck for adoption?", "5 ducks for adoption?", "7 ducks for adoption?"
#regex \d\sducks?\sfor\sadoption\?

txt_al = "1 duck for adoption?"
txt_am = "5 ducks for adoption?"
txt_an = "7 ducks for adoption?"

al = re.match("\d\sducks?\sfor\sadoption\?", txt_al)
am = re.match("\d\sducks?\sfor\sadoption\?", txt_am)
an = re.match("\d\sducks?\sfor\sadoption\?", txt_an)

"""
regex(al)
regex(am)
regex(an)
"""

#Quantifiers - 0 or more, 1 or more - Kleene

#matching "hoot", "hoooooot", "hooooooooooot" but NOT
# "hot", "hoat", "hoo"

#regex hoo+t
#regex hoo*t matches "hot" as well 

txt_ao = "hoot"
txt_ap = "hoooooot"
txt_aq = "hooooooooooot"
txt_ar = "hot"
txt_as = "hoat"
txt_at = "hoo"

ao = re.match("hoo+t", txt_ao)
ap = re.match("hoo+t", txt_ap)
aq = re.match("hoo+t", txt_aq)
ar = re.match("hoo+t", txt_ar)
as_ = re.match("hoo+t", txt_as)
at = re.match("hoo+t", txt_at)

"""
regex(ao)
regex(ap)
regex(aq)
regex(ar)
regex(as_)
regex(at)
"""

#Anchors

#matching "penguins are cooler than regular expressions" but NOT
# "king penguins are cooler than regular expressions", "penguins are cooler than regular expressions!"
#regex ^penguins\sare\scooler\sthan\sregular\sexpressions$

txt_au = "penguins are cooler than regular expressions"
txt_av = "king penguins are cooler than regular expressions"
txt_aw = "penguins are cooler than regular expressions!"

au = re.match("^penguins\sare\scooler\sthan\sregular\sexpressions$", txt_au)
av = re.match("^penguins\sare\scooler\sthan\sregular\sexpressions$", txt_av)
aw = re.match("^penguins\sare\scooler\sthan\sregular\sexpressions$", txt_aw)

"""
regex(au)
regex(av)
regex(aw)
"""