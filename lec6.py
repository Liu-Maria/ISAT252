"""
Week 2, day 6, lec 6
"""
# demo_string = 'this is my string'

# for str_item in demo_string:      #for loop
#     print(str_item)
    
# for word_item in demo_string.split():
#     print(word_item.upper())
#     print(word_item.title())
    
# for word_item in demo_string.split():       #split by each word
#     if word_item is 'my':     #print 'my' if there is one
#         print(word_item)
#     if word_item != 'my':     #leave out 'my'
#         print(word_item)
    
# for word_item in demo_string.split():       #split by each word
#     print(word_item)
#     for str_item in demo_string:
#         print(str_item)

# print(range(4))       #will print range(0, 3)     #will not print each number
# print(range(1, 3))        #not a list
# print(range(1, 6, 2))

# for each_num in range(5):       #combine with for loop to get each number
#     print(each_num)
'''
Use of breakpoint and debugging mode
Click on line number to add breakpoint
The weird green bush is for debugging
'''

num_list = [213, 321, 123, 312]

max_item = num_list[0]      #use the first item as a placeholder for the max value

'''
#Finding the max value
num_list.sort()
print(num_list[-1])
'''

for num in num_list:
    if max_item <= num:
        max_item = num
print(max_item)

# print(max(num_list))