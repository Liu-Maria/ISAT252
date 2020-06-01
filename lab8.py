"""
Week 3, lab 8
"""

#3.1
def word_count(input_str):
    return len(input_str.split())

#3.2
demo_str = 'hello world!'
print(word_count(demo_str))

#3.3
def minimal_number(input_num):
    min_item = input_num[0]
    
    for num in input_num:
        if type(num) is not str:
            if min_item >= num:
                min_item = num
    return min_item


"""
ALternative without for loop just for fun       #IT WORKS!
def minimal_number(input_num):
    the_minimal_number = input_num.sort()
    min_num = input_num[0]
    return min_num
"""

#3.4
demo_list = [1,2,3,4,5,6]
print(minimal_number(demo_list))

#3.5
mix_list = [1,2,3,4,'a',5,6]
print(minimal_number(mix_list))