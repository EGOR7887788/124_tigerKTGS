# create tuple
a = (1, 1.1, 'a', [4, 5, 6], {'a':1, 'b':2}, None, True)
a = ()
b = tuple()
b= (1,)
a = [1, 2.1, 3] # это список list
tuple(a) # (1, 2.1, 3)
b = tuple('abc') # ('a', 'b', 'c')
a = [1, 2.1, 3] # раньше я был списком
tuple(a) # (1, 2.1, 3), но 'a' остался списком
b = tuple('abc') # ('a', 'b', 'c')
# retrive tuple
a = (1, 2.1, 'd') # в кортеже можно обращаться к элементу по индексу
a[0] # 1
a[2] # ‘d’
a = (1, 1.1, 'a')
print(a) # (1, 1.1, 'a')
print((1, 1.1, 'a')) # (1, 1.1, 'a')
# update tuple