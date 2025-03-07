"""
In Python, conditions are used to execute specific blocks of code based on whether a given condition is True or False. This allows us to control the flow of a program based on logic and comparisons.

"""
"""  
In Python, we use comparison operators to compare values. These operators return True or False based on the comparison.

==: Equal to
!=: Not equal to
>: Greater than
<: Less than
>=: Greater than or equal to
<=: Less than or equal to
"""
a = 5
b = 10

c = a < b # c is a boolean
print(c)
print(type(c))

d = a > b 
print(d)
e = b > a
print(e)

a = 10
b = 10

c = a == b
print(c)

d = a >= b
print(d)

e = a > b
print(e)

f = a <= b
print(f)

g = a < b
print(g)

a = 10
b = 100

c = a != b
print(c)

a = 100
b = 100
c = a != b
print(c)


""" 
Logical operators combine multiple conditions:

and: Returns True if both conditions are true.
or: Returns True if at least one condition is true.
not: Reverses the logical state of its operand.
"""
c = 8

condition1 = c > 5
condtion2 = c < 10
isBetween5_10 = condition1 and condtion2
print(isBetween5_10)

c = 50

condtion1 = c < 30
condtion2 = c < 60
result = condtion1 or condtion2
print(result)

c = 50

condtion1 = c < 30
condtion2 = c < 60
result = condtion1 and condtion2
print(result)

c = 50

condtion1 = c < 100
result = not condtion1 # inverse condition
print(result)

a = None # check None Value
c = a is not None # is used for None Values
print(c)

a = 10 # check None Value
c = a is not None # is used for None Values
print(c)

c = 14

condition = c > 10 and c < 20 and c > 12  and c < 15

print(condition)

c = 15

condition = c > 10 and c < 20 or  c > 50  and c < 100
#condition = (c > 10 and c < 20) or  (c > 50  and c < 100) # the same
print(condition)

condition = 10 < 20 or (20 > 10 or 50 < 100) and 100 < 1000 # () has the highest priority

""" The if statement allows us to check whether a condition is true or false and execute code accordingly. """
a = 10
if a < 20:
    print("a is less than 20") # this line will be executed since 10 < 20
print("suite du code")

""" The else statement is used to specify a block of code to run when the if condition is not true. """

ennemies = 10
if ennemies <= 1:
    print("take risk")
else:
    print("revive")

"""The elif (else if) statement allows us to check multiple conditions. It's useful when you want to check more than two conditions."""

a = 10
if a == 2:
    print('is 2')
elif a == 3:
    print('is 3')
elif a == 4:
    print("is 4")
else:
    print("other")

a = 12
if a > 10 and a < 20:
    print("a is > 10 and < 20")
else:
    print('not in')

if 10 < a < 20: # the same as above
    print("a is between 10 and 20")

liste = [1,2,3,4,5]

if 3 in liste:
    print('3 in liste')

if 10 not in liste:
    print('10 not in liste')

if True:
    print("is true")

mylist = [1,2]
if mylist: # check if the list is not empty
    print("list is not empty")

mydict = {"key1": 10, "key2": 20}

if mydict:
    print("my dict is not empty")

if "key1" in mydict.keys(): # check if a key exists
    print("key 1 exists")

if 10 in mydict.values(): # check if a value exists
    print("10 exists")

# nested if, you can define multiples if inside if block
a = 10
if a < 20:
    if a < 15:
        if a < 12:
            print(a)
        else:
            print('else')