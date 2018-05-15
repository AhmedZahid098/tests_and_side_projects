# Decimals are also the type in python. Without using 'decimals' library, floats would
# only give you the 'precise' or closest value but not the acurate one.
# Try not to use money and scientific related problems with normal float type
# instead use 'decimal' library for calculations, you want acuracy.

# Floating point
print(1 / 3)
print(1 / 2 + 2 / 3)

# Decimals fixed prescion
import decimal
d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 3
print(decimal.Decimal('100.000') / decimal.Decimal('300.000'))

# Fraction function --> Fraction(numerator, denominator)
from fractions import Fraction
f = Fraction(2, 3)
print(1 + f)
print(f + 55)

# Booleans
print(1 < 2 < 5)
print(bool('spam'))

# 'None'
print(type(None))
print(help(None))
print(dir(None))
x = None
print(x)
l = [None] * 4
print(l)
