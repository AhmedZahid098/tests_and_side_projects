# Dictionaries are not a sequences but are 'mapping'
D = {'food': 'spam', 'quantity': 4, 'colour': 'pink'}
print(D)
# Changing and calling values is as below
print(D['food'])

D['quantity'] += 1
print(D)

D['food'] = 'jam'
print(D)

# Another way of creating a Dictionaries
D = {}
D['name'] = 'Ahmed'
D['age'] = 25
D['job'] = 'developer+engineer'
print(D)

# Creat dict using keys --> variable = dict(key = value)
bob1 = dict(name='Ahmed', job='developer', age=40)
print(bob1)

# Don't worry about the order of the keys and values typed and printed that is python version speciefic
# Make dict using zipping --> variable = dict(zip([key1, key2, ...], [value1, value2, ...]))
bob2 = dict(zip(['name', 'job', 'age'], ['Ahmed', 'developer', 40]))
print(bob2)

# Nesting in dict
rec = {'name': {'First': 'Ahmed', 'Last': 'Zahid'},
       'job': ['developer', 'engineer'],
       'age': 25.1}
print(rec)

# calling nested Dictionaries
print(rec['name'])
print(rec['job'])
print(rec['age'])

# calling nested dict through indexing
print (rec['job'][-1])
print (rec['name']['First'])

# Appending the nested dict->because job is in list
rec['job'].append('Ummati')
print(rec['job'])

# Assigning new values to dict using key
D['religion'] = 'Islam'
print (D)

# Refrecing a non-existent dict would give an error instead use 'if' command
print('f' in D)

# OR
if not 'f' in D:
    print ('missing')

# Sorting dict in loop
D = {'a': 1, 'b': 2, 'c': 3}
print (D)

ks = list(D.keys())
print (ks)

ks.sort()
print(ks)

for key in ks:
    print(key, D[key])

# Anaother way of sorting dict through keys --> short method
for keys in sorted(D):
    print(key, D[key])

# Using 'While Loop' other than Dictionaries
x = 0
while x < 5:
    print('spam!' * x)
    x += 1
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1
