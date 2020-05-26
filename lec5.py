"""
week 2, day 5, lec 5
"""
# import this       #Zen statement
# print(1 + 2)        #spaces are ignored
# print([1, 2, 3,

# 4, 5, 6] )
# m = 1\          #Use the backslash to use more than one line
# +2
# print(m)

# a = 123
# print(a)
# print(id(123))      #They have the same id
# print(id(a))

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)       #same values
# print(a is b)       #different id
# print(id(a))
# print(id(b))

# x = None
# print(id(None))
# print(id(x))
# print(x is None)      #The same id

# y = []          #An empty list
# print(y == None)    #Only None is None

# print(True)         #Boolean types
# print(False)        #Boolean types

# print(True and False)
# print(True or False)
# print(not False)
# print(not True)

# print(not None)
# print(not '0')      #o is false, empty strings are false, but '0' is true
# print(not 0)        #integer 0 is considered false
# print( () and [] )      #empty data containers are all considered false       #if x is false, it will return x
'''
empty data containers, integer 0, float 0.0, None are all considered false
'''

# if 2>1 : 
#     if 1.5>1 :
#         print('1.5>1')
#     print('2>1')

# if 2<=1 :
#     print('2<=1')
# else:
#         print('2>1')

# if 2<=2 :
#     print('2<=2')
# else:
#     print('2>1')

# if 2<=1:
#     print('2<=1')
# elif 2<=2:
#     print('2<=2')
# else:
#     print('2>1')

if None:
    print(1)
elif {}:
    print(2)
elif '0':
    print(3)
else:
    print(4)