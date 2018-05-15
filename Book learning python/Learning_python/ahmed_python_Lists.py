# Creating a list
L = [123, 'spam', 1.23]
print(L)
print(len(L))

# Indexing
print(L[0])

# slicing
print(L[:1], L[:-1])

# concatination
print(L + [4, 5, 6])

# repeating in a list
print(L * 2)

# lists have no fixed size, they can grow and shrink on demand
# Growing a list at an end
L.append('Ali')
print(L)

# Another way of growing a list --> list.insert(index, obj)
L.insert(4, 'B')
print(L)

# Shrinking a list through Indexing
L.pop(4)
print(L)

# Another way of shrinking
del L[3]
print(L)

# other way of shrinking --> list.remove(object)
L.remove('spam')
L.remove(1.23)
L.remove(123)
print(L)

# storing in acending fashion --> list.sort()
L = ['dd', 'ee', 'cc', 'bb', 'aa']
L.sort()
print(L)

# sorting in decending fashion --> list.reverse()
L.reverse()
print(L)

# Supports arbitrary nesting eg: 3*3 matrix
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print (M)

# We can call certain value by Indexing --> list[row index][col index]
print(M[0][0], M[0][1], M[0][2], M[1][0], M[1][1], M[1][2])

# Comprehensions are way to call list values --> variable = [row[index] for row in list]
col1 = [row[0] for row in M]
print (col1)

# Manipulating matrix
# Adding a number to the values of matrix
M_col = [row[1] + 1 for row in M]
print(M_col)

# Even or odd numbers
M_col = [row[2] for row in M if row[2] % 2 == 0]
print(M_col)

# Diagnol of a matrix
M_col = [M[i][i] for i in [0, 1, 2]]
print(M_col)

# Multiplicating types
M_col = [int * 2 for int in M]
print(M_col)

M_col = [c * 2 for c in 'spam']
print(M_col)

# Ranging lists
print(list(range(6)))

# Another way for ranging lists --> list(range(initial, final, offset))
print(list(range(-5, 6, 3)))

# Multiple values
print([[x**2, x**3] for x in range(4)])

# Multiple values with 'if' statement
print([[x, x / 2, x * 2] for x in range(-5, 6, 3) if x > 0])

# Using lists and Creating Generators through Comprehensions
G = (sum(row) for row in M)
print(next(G), next(G), next(G))

# Creating a list in 'set' of row using '{ }' for set
s = {sum(row) for row in M}
print(s)

# Creating a key/value table of row sums
s = {i: sum(M[i]) for i in range(3)}
print(s)

# List Comprehensions expressions for an iterabkle object
cubes = [x ** 3 for x in [1, 2, 3, 4, 5]]
print (cubes)

# above and below both run iteration protocol internally
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
    print (squares)
# Last print statement is in loop intentionally so you may get to know how the loop works
