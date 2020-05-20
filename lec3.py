"""
Lecture notes for week 1, day 3
"""
# my_list = [1, 2, 3, 4, 5]

# print(my_list)

#my_nested_list = [1,2,3,my_list]
#print(my_nested_list)

#print(my_list[0])  #0 is the first item of the list by index
# my_list[0] = 6    #you can change the items in your list by place
# print(my_list)

#print(my_list[-2])  #negatives numbers will start from the last number

#print(my_list[0:2])     #print the list from 0 to 2 (the last one will not be printed)
# print(my_list[3:])

# my_list.append(7)
# my_list.append(7)   #adds another 7
# print(my_list)
# my_list.remove(7)
# print(my_list)

# my_list.sort()      #Sorts the list in ascending order
# print(my_list)
# my_list.reverse()   #Sorts the list in descending order
# print(my_list)

# print(my_list + [8, 9])
# my_list.extend([8, 9, 'a', 'b'])    #requires [ ] brackets
# print(my_list)

# print(6 in my_list)     #returns True
# print(0 in my_list)     #returns False
# print('6' in my_list)   #returns False because it is not a string in the list

# print(len(my_list))     #shows the number of items in a list





# my_letters = ['a', 'b', 'c']
# print(my_letters[0:2])

# x,y,z = ['a', 'b', 'c']
# print(x)
# print(y)
# print(z)


# print('hello world')
# print('hello\tworld')
# print('hello\nworld')
# print(len('helloworld'))
# print(len('hello world'))
# print('helloworld'[0])

my_letters = ['a', 'a', 'b', 'b', 'c']
print(my_letters)
my_unique_letters = set(my_letters)
print(my_unique_letters)