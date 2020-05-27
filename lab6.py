"""
Week 2, day 6, lab 6
"""

#3.1
for each_num in range(0, 6):     #numbers 0 to 5
    if each_num is not 3:       #don't count 3
        print(each_num)         #exclude 3 and 6

#3.2
i = 1                       #set another variable
for num in range(1, 6):     #from 0 to 5
    i = i*num               #multiplying the numbers
print(i)

#3.3
i = 0
for num in range(1,6):      #range from 1 to 5
    i = i+num               #getting the sum
print(i)

#3.4
i = 1
for num in range(3, 9):     #range from 3 to 8
    i = i*num               #multiply
print(i)

#3.5
i = 1                       #set the dividend
for num in range(1, 9): 
    i = i*num
k = 1                       #set the divisor
for num in range(1, 4):     
    k = k*num
print(i)
print(k)
print(i/k)                  #get the quotient

#3.6
my_string =  'this is my 6th string'    #def string
k = 1                                   #adding one to number of spaces
for i in my_string:                     
    if i is ' ':                        #count the number of spaces
        k = k + 1
print(k)
'''
Alternative:
i = 0
for word in 'this is my 6th string'.split():
    i = i + 1
print(i)
'''

# #3.7
my_tweet = {
"favorite_count":1138,
"lang": "en",
"coordinates": (-75, 40),
"entities": {"hashtags": [" Preds ", "Pens", " SingIntoSpring "]} }

i = 0
for hashtags in my_tweet['entities']['hashtags']:
    i = i + 1
print(i)