"""
Wk 1, Day 4, lec 4
"""
my_tuple = 'a', 'b', 'c', 'd', 'e'
# print(my_tuple)

# my_2nd_tuple = ('a', 'b', 'c', 'd', 'e')    #Python does not care about parentheses 
# print(my_2nd_tuple)

# test = ("a",)
# print(type(test))       #The comma defines a tuple

# print(my_tuple[1:5])        #Choose which of the list to show by index

my_car = {
            'color':'red',
            'maker':'toyota',
            'year': 2015
                                }
# print(my_car)
# print(my_car['color'])      #Getting an individual value
# print(my_car['year'])
# print(my_car.items())
# print(my_car.keys())       #Returns all the keys
# print(my_car.get('year'))   #get a single value

# my_car['model'] = 'corolla'   #Adding a new key and value
# print(my_car)
# my_car['year'] = 2020       #Changing the year
# print(my_car)

print('color' in my_car)
print('gas' in my_car)