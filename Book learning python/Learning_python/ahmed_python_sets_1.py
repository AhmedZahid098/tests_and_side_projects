# Sets are unordered collections of unique and immutable objects, sets are useful for common tasks
# such as filtering out duplicates, isolating differences, and performing order-neutral
# equality tests without sorting in lists, strings, and all other iterable objects
# Creating sets --> set('elements') or {'elements'}

X = set("ahmed")
print(X)
Y = {'z', 'a', 'h', 'i', 'd'}
print(Y)

# Intersection --> set1 & set2
print(X & Y)

# Union --> set1 | set2
print(X | Y)

# Difference --> set1 - set2
print (X - Y)
print (Y - X)

# Superset --> set1 > set2
print(X > Y)
print(Y > X)

# Sets filter out the duplicate elements
print({1, 2, 3, 1, 2, 3})

# Ordered neutral eqaulity test
print({'spam'} == {'aspm'})

# Membership test
print('a' in X)
print ('z' in Y)
print('p' in set('spam'))
