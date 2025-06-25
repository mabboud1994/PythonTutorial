## A function is a block of organized, reusable code that performs a single, related action. It helps reduce repetition and make code easier to manage and debug.

""" def function_name ():
        logic
"""
def greet():
    print("Hello world")

greet() # call the function greet

"""
Definition:
Parameter: A variable in the function definition.

Argument: The actual value passed to the function when calling it.
"""
def myFunction1(name):
    print(f"hello {name}")
    #print("hello {}".format(name)) # same

myFunction1("mahmoud")
myFunction1("ahmad") # i reuse it with different argument
myFunction1(["mahmoud", "ahmad"]) # the type of the parameter is defined according to the argument passed to function


def getMaxInList(aList):
    """ Safe Check """
    if type(aList) != list:
        return "the given param is not a list"
    for elem in aList:
        if type(elem) != int:
            return "the list contains a least one non integer item"
    """ Get the max logic """
    max_in_list = aList[0]
    for elem in aList:
        if elem >= max_in_list:
            max_in_list = elem
    return max_in_list

max_result = getMaxInList([-100,-2,-3])
print(max_result)
max_result = getMaxInList([1,2,"ll"]) # not pass
print(max_result)
max_result = getMaxInList(dict()) # not pass
print(max_result)

def calc(a, b):
    return a+b, a-b # return a tuple (a+b, a-b)

mysum, mydiff = calc(5,3)
print(mysum, mydiff)

myresult = calc(5,3)
mysum = myresult[0]
mydiff = myresult[1]
print(mysum, mydiff)

def MyExample(name="Mahmoud", surname="Ahmad"):
    print(name, surname)

MyExample()
MyExample(name="Ahmad")
MyExample(name="khaled", surname="Samir")

def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5))

def show_stat(**kwargs):
    if "damage" in kwargs.keys():
        print(f"your damage is {kwargs["damage"]}")
    if "health" in kwargs.keys():
        print(f"your health is {kwargs["health"]}")

show_stat(damage=10, health=90)
show_stat(damage=10)

a = 20 # variable global
def ScopeFunc():
    a = 10 # variable locale
    print(a)

ScopeFunc()