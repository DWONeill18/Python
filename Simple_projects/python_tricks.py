# python tricks

# function to comment if a number is even
def is_even(x):
    if x %2 == 0:
        return True
    else:
        return False

print(is_even(900))

# We’ll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0
def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False

# Test an integer without using type()
from math import *
def is_int(x):
    if floor(x)-x==0: #here you can use “ceil” instead of "floor"
        return True
    else:
        return False

print(is_int(6))
print(is_int(6.5))
#print(is_int(hello))

# Add the digits of a number to calculate the sum
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        print(x)
    return total

print(digit_sum(1234))

# Calcukate tghe factoruial of a non negative integer
def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total

print(factorial(5))

# Testing for a prime number
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print(is_prime(17))

# Reverse a string
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print(reverse("Hello World"))

