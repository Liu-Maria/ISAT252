"""
Week 2, day 7, lec 7
"""

# i = 5
# while i >= 0:
#     i = i - 1
#     if i == 3:
#         # break         #breaks the smallest loop
#         # continue      #skips the current iteration and moves on
#         # pass          #does nothing, but is placehold if you need something for syntax
#     print(i)

# for word in 'hello world'.split():
#     print(word)
#     for str_item in word:
#         if str_item == '1':
#             break
#         print(str_item)

# try:
#     print(1/0)
# except ZeroDivisionError:
#         print('error')

i = 5
while i >= 0:
    try:
        print(1/(i-3))
    except:
        pass
    i = i - 1