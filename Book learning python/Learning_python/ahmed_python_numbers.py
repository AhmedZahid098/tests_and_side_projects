# Addition and multiplication is covered in precious chapter of the book
# True and false statements are customized statements of 0 and 1
# There are two main types of divisions in python --> classic and floor
# Classic divison --> '/' returns decimal
# floor divison --> '//' returns integer
import math
print(5 / 2)
print(5 // 2)
print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))

# Octal literals
print(0o10)

# Binary literals
print(0b111)

# Hex literals
print(0xf)

# Here is an example of all the conversions
# binary conversion didn't work
print('%o, %x' % (64, 64))

# Floor for rounding decimal numbers
print(math.floor(2.567), math.floor(-2.567))

# trunc for rounding decimal numbers
print(math.trunc(2.567), math.trunc(-2.567))

# integer rounding decimal numbers
print(int(2.567), int(-2.567))

# round for rounding decimal numbers
print(round(2.567), round(-2.567))

# roumding for the display--> '%.(decimal places)f' %decimal numbers
print('%.1f' % 2.567)  # note --> it produce strings
