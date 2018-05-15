# There are three ways to tests type in python

L = [None]
# using type syntx
if type(L) == type([]):
    print('yup')

# using type name
if type(L) == list:
    print('yup')

# using object orient test
if isinstance(L, list):
    print('yup')
