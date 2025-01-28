# it is a one line comment

""" this is a multiline 
comment """

''' this is also
multiline comment'''

print("begin of code ") # it is a print function

""" Identation """
if True:
    print("first command of if") # the identation define a scope of code
    print("second command of if") # select a pice of code then click on Tab (this will add an identation), inverse: select the pice of code then do a shift + Tab
print("outside of if")

"""
The Data Types of Python (Primitive or built-in (By Default))

Text Type:	str (String)
Numeric Types:	int (Entier no comma), float (all numbers), complex
Sequence Types:	list, tuple, range
Mapping Type:	dict (dictionnaire)
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview # not a big deal to know this types
None Type:	NoneType
another types:
User Defined Types: Created by user or provided by a third-party library
# Good to know: a definition of a type is done by using a python object named class
"""
#### Important Note: Python does not require type definition before variable declaration
#### Important Note: Python variable names is case-sensitive (myvar is not the same variable named Myvar)


name = "Mahmoud" # this is a string, variable declaration provides you with a reference to data (it allows you to call this data from anywhere)
print(name)
#print(Name) # variable name is case sensitive
#2a = 1 # variable name cannot begin with number
a2 = 1 # it is ok
#my-var = "" # variable name cannot contains special characters
my_var = "" # you can use underscores

#print(x) # you cannot use a reference to a variable before declaring it
#x = 1


age = 31 # this is an int
print(age)

adresse = "8" # this is a string
print(adresse)

percentage = 33.8 # this is a float
print(percentage)

nb_complex = complex(2, 5) # this is a complex
print(nb_complex)

#topScores = [] # this is an empty list
#print(topScores)
#topScores = [1,2,3,4,5] # you can fill up the list when declaring it
#print(topScores)
topScores = [1,"mahmoud",3,"ahmad",5.7] # list can contains any data types
print(topScores)

myTuple = (1,2,3,4,5) # this is a tuple, basically, tuples are used as a variable type that represent the return value of a function when this function returns more than one variables
print(myTuple)

myRange = range(100) # (0 to 99) this is a range, used to produces a sequence of integers from start(inlusive) to end (exclusive), if the start is omitted by user then the default start value is 0
RangeWithStart = range(20, 100) # (20 to 99) this is a range with a start value defined by user.
print(myRange)

mydict = {} # this is an empty dict (a dict is an object that map keys to values)
mydict = dict() # this is also an empty dict
person = {"name": "mahmoud", 2: "test", "adresse": "8 sq de nimegue"} # you can fill up dict when declaring it.
print(person)

mySet = {2,5,7,4,4,4,4} # the same as list, except that it not allow occurence
mySet.add(10) # normal set accept add and remove elements
print(mySet)

frozenMyset = frozenset({2,5,10}) # the same as set except that frozen set does not allow user to add or remove elements
print(frozenMyset)

#isThisListEmpty = True # this is a bool (basically, booleans are used in condition, like if conditon)
isThisListEmpty = False # this is a bool
print(isThisListEmpty)

myNone = None # this is a None Variable (None means no type)
print(myNone)

""" Verify types """

print("the type of name is: ", type(name))
print("the type of age is: ", type(age))
print("the type of adresse is: ", type(adresse))
print("the type of percentage is: ", type(percentage))
print("the type of nb_complex is: ", type(nb_complex))
print("the type of topScores is: ", type(topScores))
print("the type of myTuple is: ", type(myTuple))
print("the type of person is: ", type(person))
print("the type of mySet is: ", type(mySet))
print("the type of frozenMyset is: ", type(frozenMyset))
print("the type of myNone is: ", type(myNone))
print("the type of myRange is: ", type(myRange))

"""   Variables assignements   """
ennemies = 10
friends = 5
print("the old value of friends before assignement ",friends)
friends = ennemies # the new value of friends equal the value of enemies
print("the new value of friends after assignement ",friends)

ennemies = 10
print("the type of ennemies before assignement is int", ennemies)
ennemies = "10 ennemies"
print("the type of ennemies after assignement is str", ennemies)

"""  Variable Casting  """
nombre = 13.7 # this is a float
print(nombre)
result = int(nombre) # cast float number to int, this will remove any number after dot
print(result)

nombrestr = "105"
result = int(nombrestr) # result now is an int that can be used in calculus
print(result)

#nombrestr = "hello"
#result = int(nombrestr) # this will raise an error because base number is not a numeric string
#print(result)

nombre = 13 # this is an int
print(nombre)
result = float(nombre) # cast int number to float, this will add .0 to 13
print(result)

nombrestr = "105.7"
result = float(nombrestr) # result now is an float that can be used in calculus
print(result)

dict = {"name": "mahmoud"} 
result = str(dict) # result now is a str that can be printed
print(result)

myStr = "hello world" 
result = list(myStr) # result now is a list while each character of hello world  is an elemenet of list
print(result)

myRange = range(101)
mylist = list(myRange) # list will fill up a list from 0 to 100
print(mylist)

"""  Input  """
name = input("Give me your name") # the provided user input will be stored in the name variable
print("your name is: ", name)