"""
week 2, day 5, lab 5
"""

#3.1
alien_color = 'green'

if alien_color is 'green':
    print('You have earned 5 points')
    
#3.2
alien_color = 'yellow'

if alien_color is 'green':
    print('You have earned 5 points')
else:
    print('You have earned 10 points')

#3.3
favorite_fruits = ['pineapple', 'passionfruit', 'mango', 'kiwi', 'guava']

if 'pineapple' in favorite_fruits:
    print('In a world full of apples, it is much better to be a pineapple.')

if 'coconut' in favorite_fruits:
    print('Coconut lover since day one.')
    
if 'mango' in favorite_fruits:
    print('It takes two to mango.')
    
if'kiwi' in favorite_fruits:
    print('Kiwi be friends?')
    
if 'melon' in favorite_fruits:
    print("You're one in a melon!")


#3.4
person = 35

if person < 10:
    print("You're a kid!")
elif person >= 10 and person < 20:
    print("You're a teenager!")
elif person > 20:
    print("You're an adult!")
    if person > 65:
        print("You're an elder!")

