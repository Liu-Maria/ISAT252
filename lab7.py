"""
Week 2, day 7, lab 7
"""
3.1
i = 0
while i <= 6:
    if i == 3 or i == 6:
        i = i + 1
        continue
    print(i)
    i = i + 1

#3.2
i = 5
factorial = 1
while i > 1:
    factorial = factorial*i
    i = i - 1
print(factorial)

#3.3
i = 1
factorial = 0
while i <= 5:
    factorial = factorial + i
    i = i + 1
print(factorial)

#3.4
i = 3
factorial = 1
while i <= 8:
    factorial = factorial*i
    i = i + 1
print(factorial)

#3.5
i = 1
dividend = 1
while i <= 8:
    dividend = dividend*i
    i = i + 1
print(dividend)
i = 1
divisor = 1
while i <= 3:
    divisor = divisor*i
    i = i + 1
print(divisor)
print(dividend/divisor)

#3.6
num_list = [ 12, 32, 43, 35]
while num_list:
    num_list.remove(num_list[0])
    print(num_list)
"""
#Using other methods
print(len(num_list))
while len(num_list) != 0:
    num_list.pop(0)
    print(num_list)
"""