"""        Data Manipulation: Numbers and Strings              """


"""
Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations

Syn Name        Example

+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

"""
a = 1 + 2 # the value of a is 3
a = 1*2 # the value of a is 2
a = 1/2 # the value of a is 0.5
a = 1%2 # the value of a is 1
a = 4%2 # the value of a is 0
a = 2**2 # the value of a is 4
a = 7 // 2 # the value of a is 3 (same as int(7/2))


"""
Python Assignment Operators
Operator Example  Same As
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3

"""
a = 1
a += 1 # a is 2
a-=1 # a is 1
a *= 2 # a is 2
a /=  2 # a is 1
a %=2 # a is 1

# PEMDAS: https://en.wikipedia.org/wiki/Order_of_operations#:~:text=The%20acronym%20PEMDAS%2C%20which%20stands,Excuse%20My%20Dear%20Aunt%20Sally%22
a = 4/2 + 5**2/3 # value is : 10.333333333333334, if the expression does not contain (), python treats the expression as defined in PEMDAS rules
a = (4/2) + 5**(2/3) # value is: 4.924017738212866, the priority is for ()


# You can join two or more strings together using the + operator.

string1 = "hello "
string2 = "world "
string3 = ", iam here"
result = string1 + string2 + string3
#result = "ddd" + "sss" + "vvv" # alternative implementation
print(result)

#You can repeat a string multiple times using the * operator.
result = result*3
#result = "my string"*3 # alternative implementation
print(result)

# Strings can be sliced using indexing (see StringIndexing.png), allowing you to extract a portion of a string
String = "Hello, world"
Substring = String[7:] # no input on the right of : means that the slicing must go to the end of string
Substring = String[7:12] # here the substring goes from index 7 to 12 excluded
print(Substring)

#upper() converts all characters to uppercase.
String = "hello,-"
result = String.upper() # special characters are ignored
print(result)

#lower() converts all characters to lowercase.
String = "HeLlo,-"
result = String.lower() # special characters are ignored
print(result)

#capitalize() capitalizes the first character.
String = "hello world"
result = String.capitalize()
print(result)

#title() capitalizes the first letter of each word.
String = "hello world"
result = String.title()
print(result)

#swapcase() swaps the case of all characters.
String = "HeLlo World"
result = String.swapcase()
print(result)

#strip() removes leading and trailing whitespace from a string.
String = "   hello world   "
result = String.strip()
print(result)

# lstrip() removes leading whitespace.
String = "   hello world   "
result = String.lstrip()
print(result)

#rstrip() removes trailing whitespace.
String = "   hello world   "
result = String.rstrip()
print(result)

#The len() function gives the length of a string.
String = "hello"
result = len(String)
print(result)

#find() returns the index of the first occurrence of a substring (returns -1 if not found).
String = "hello world world"
result = String.find("world")
result = String.find("world", 0,5) # if starts and end indices are specified, then the find processes the search on this piece of string only
print(result)

#rfind() returns the index of the last occurrence of a substring.
String = "hello world world"
result = String.rfind("world") # can take also start and end indices
print(result)

# replace() replaces a substring with another substring.
String = "hello world"
result = String.replace("world", "There") # replace first occurence only
print(result)

String = "hello world world"
result = String.replace("world", "There")
print(result)

String = "hello world world world"
result = String.replace("world", "There", 2) # replace the first 2 occurences
print(result)

"""  To explain next session: i put them here to make a full release on github """

# split() divides a string into a list of substrings based on a delimiter.
string = "apple,banana,cherry"
result = string.split(",")  # Output is a list: ['apple', 'banana', 'cherry']

#splitlines() splits a string into a list at line breaks.
string = "Hello\nWorld" # \n in string mean that there is a break line here
result = string.splitlines()  # Output: ['Hello', 'World']

#join() combines a list of strings into a single string using a delimiter.
fruits = ["apple", "banana", "cherry"] # a list of string
result = ", ".join(fruits)  # Output is a string: "apple, banana, cherry"

#startswith() checks if the string starts with a certain substring.
string = "Hello, World!"
result = string.startswith("Hello")  # Output is a bool: True

#endswith() checks if the string ends with a certain substring.
string = "Hello, World!"
result = string.endswith("World!")  # Output is a bool: True

#isalpha() checks if all characters are alphabetic.
string = "Hello"
result = string.isalpha()  # Output is a bool: True

#isdigit() checks if all characters are digits.(numbers)
string = "12345"
result = string.isdigit()  # Output is bool: True

# Formatting Strings
#Using f-strings (Python 3.6+):
name = "Alice"
age = 30
result = f"Name: {name}, Age: {age}"  # Output: "Name: Alice, Age: 30"
#Using format() method:
result = "Hello, {}!".format("Alice")  # Output: "Hello, Alice!"

#Escaping Characters
#You can escape special characters using a backslash (\).
string = "He said, \"Hello!\""  # Output: He said, "Hello!" # note that this is the only way to define a " or ' into a string as characters of string