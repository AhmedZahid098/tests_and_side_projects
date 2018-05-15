# Tuples are sequences, like lists, but they are immutable, like strings
# Syntactically, they are normally coded in parentheses instead of square brackets,
# and they support arbitrarytypes, arbitrary nesting, and the usual sequence operations.

# A Tuple and its length is as below
T = (1, 'a', 2, 'b', 3, 'c')
print (T)
print(len(T))

# Indexing
print(T[2])

# slicing
print(T[3:])

# Concatination didn't happen
T = T + ()
print(T)

# Method of Tuple --> tuple.index(index) --> didn't work
a = T.index(2)
print(a)

# Method of Tuple --> tuple.count(index) --> didn't work
a = T.count(1)
print(a)

# Cannot grow and shrink the tuples although it is possible use nesting
