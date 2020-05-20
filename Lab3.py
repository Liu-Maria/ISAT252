"""
Week 1, Day 3, Lab 3
Maria Liu
"""

#3.1
str_list = ['a', 'd', 'e', 'b', 'c']
print(str_list)
str_list.sort()     #sorts it alphabetically
print(str_list)

#3.2
str_list.append('f')    #adds 'f' to str_list
print(str_list)

#3.3
str_list.remove('d')    #removes 'd' from str_list
print(str_list)

#3.4
print(str_list[2])      #prints the 3rd item by idex, which is 'c'

#3.5
my_list = ['a', '123', 123, 'b', 'B', 'False', False, 123, None, 'None' ]
print(my_list)
print(len(my_list))     #looks at the length of  my_list
print(set(my_list))     #turns it into a set and eliminted repeats
print(len(set(my_list)))    #prints the length of the set, which is also the number of unique items in my_list

#3.6
print(len("This is my third python lab."))  #prints the number of characters inclusing spaces
print(len(["This", "is", "my", "third", "python", "lab."]))     #prints the number of items, which is the number of words

#3.7
num_list = [12, 32, 43, 35] 
num_list.sort()     #Sorts the list in ascending order
print(num_list[0])      #prints the first item, which is also the minimal value
print(num_list[-1])     #prints the last item, which is also the maximal value
'''
alternatively:
num_list.reverse        #print the list in descending order
print(num_list[0])      #print the first item again which is now the minimal value
'''


#3.8
game_board = [ [0,0,0], [0,0,0], [0,0,0]]   
print(game_board)
game_board[1] = [0, 1, 0]       #switching the second item with [0, 1, 0]
print(game_board)
