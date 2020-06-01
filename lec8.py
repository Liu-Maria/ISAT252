"""
Week 3, lecture 8
"""

# def my_function(a, b):      #you can give them a default value
#     result = a + b      #when you see variables a and b, add them together and store the sum in result
#     print('a is', a)
#     print('b is', b)
#     return result       #returns the 'result', MUST BE LAST STATEMENT
# print(my_function(1, 2))    #will return 3 #ORDER MATTERS
'''
Alternative to make it clear
print(my_function(b = 2, a = 1))
'''

# def my_function(a, b = 0):      #you can give them a default value such as b = 0, but it can be overridden when you call the function
#     result = a + b      #parameters are local, CANNOT be called outside the function
#     return result
# print(my_function(1)+1)   #the default is used if nothing else is requested


# def my_function(a, b = 0):      #you can give them a default value such as b = 0, but it can be overridden when you call the function
#     result = a + b
#     print('a is', a)
#     print('b is', b)
# print(my_function(1))       #no return, so the answer is none

# def my_function(a, b = 0):    
#     return result
#     result = a + b
#     print('a is', a)
#     print('b is', b)
# print(my_function(1, 2))


# def calculate_abs(a):         #calculated the absolute value of a number 
#     if a>0:
#         return a
#     if a<0:
#         return -a
# print(calculate_abs(0))         #Not defined to a return 
# # print(calculate_abs('a'))           #Wrong data type


# def calculate_abs(a):
#     if type(a) is str:
#         return('wrong data type')
#     if a>0:
#         return a
#     if a<0:
#         return -a
# print(calculate_abs('a'))           #Wrong data type   


##EX 2
# def calculate_sigma(m, n):
#     outer = n + m
#     multiple = m - n
    
#     result = set()


def cal_sigma(m , n):
    result = 0
    for i in range(n, m):
        result = result + i
    return result
print(cal_sigma(5, 3))


def cal_pi (m, n):
    '''
    calculate sigma(n, m)
    '''
    result = 1
    for i in range(n, m + 1):
        result = result*i
    return result
print(cal_pi(5, 3))

##Ex3

def cal_f(m):
    if m == 0:
        return 1
    else:
        return m *cal_f(m-1)
# print(cal_f(3))

def cal_p(m, n):
    return cal_f(m)/cal_f(m-n)
print(cal_p(5, 3))