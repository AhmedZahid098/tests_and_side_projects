# Importing builtin Libraries
import math
import random
import sys
import re

# Printing System Detail
print (sys.platform)

# Two raised to the power hundred
print (2**100)

# Printing string multiple times
x = 'spam!'
print (x * 8)

# Length of two to the power a million as a string
a = len(str(2**1000000))
print(a)

# Two rasied to the power four
print(2**4)

# Printing Pi value through Math Libraries
print(math.pi)

# Printing value through random command
random.random()
print(random.choice([1, 2, 3, 4, 5]))

# Printing string using indeces as in list
print(len(x), x[0], x[1], x[2], x[3], x[4], x[1:3], x[:-2])

# Printing list
print(list(x))

# Using commands find and replace
print(x.find('pa'), x.replace('pa', 'xy'))

# Printing Directory of all commands available for the variable "x"
print(dir(x))

# Numbers, Strings and tuples are immutable <--> dictionaries, Sets and list are not immutable
# We change them by creating a new value and variable
x = 'z' + x[1:]
print(x)

# Split string into substrings --> .split
line = '\naaa,bbb,cccc,dd\n'
print (line.split(','))

# Performing case conversion --> .upper or .lower
print("upper case-->"+x.upper())
print("lower case-->"+x.lower())

# Testing the content --> .isalpha or .isdigit etc
print(x.isalpha())
print(x.isdigit())
print(x.istitle())

# Strip whitespace of the side --> .rstrip or lstrip
print(line.rstrip())
print(line.lstrip())

# Combine two operation --> .rstrip().split()
print(line.rstrip().split(','))

# Help function can be called to know about any method --> Help()
help(x.replace)

# 'string'.encode('utf8') --> for storing string in 4 bytes
print('spam'.encode('utf8'))
# 'string'.encode('utf16') --> for storing string in 10 bytes
print('spam'.encode('utf16'))

# Pattern through re(regular expression) module
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))
