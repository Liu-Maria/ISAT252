"""
Week 3, Day 9, Lecture 9
Class
"""
##
##
'''
DEFINE A CLASS
'''
class car:                  #car is the name of the class
    maker = 'toyota'        #attribute
    def report_maker(self):     #method     #need 'self', representing itself?...
        return(self.maker)

my_car = car()              #Creste an instance/object
# print(my_car.report_maker())


'''
INIT METHOD
'''
class car:                  #car is the name of the class
    maker = 'toyota'        #attribute
    def __init__(self, input_model):    #Define a unique attribute 
        self.model = input_model

my_corolla = car('corolla')         #Create instances with different attributes
# print(my_corolla.maker)
# print(my_corolla.model)

my_highlander = car('highlander')
# print(my_highlander.maker)
# print(my_highlander.model)



'''
MAKING AN INSTANCE
'''
class car:                  #car is the name of the class
    maker = 'toyota'        #attribute
    def __init__(self, input_model):    #Define a unique attribute 
        self.model = input_model
    def report(self):
        #return the attribute of instance
        return self.maker, self.model

my_corolla = car('corolla')  
# print(my_corolla.report())

my_car = car('corolla')
my_car.maker = 'ford'
# print(my_car.report())          #INSTANCE CAN BE CHANGED
