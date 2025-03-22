
# to manipulate time we need to import built-in librairies
from datetime import datetime, timedelta
import time

"""
1. Introduction to Loops
Python loops repeat code blocks.
Two types: for and while.

"""
# loop through a list
names = ["tom", "jerry", "spike"]

for name in names:
    print(name)

print("main code")

# loop using range
for i in range(10,101):
    print(i)

# while loop is conditionned
i = 2
while i <= 20:
    print(i)
    i = i+2

# break is used to exit a loop
for i in range(0,101):
    if i == 5:
        break
    print(i)
# continue is used to skip an iteration
print("====================================")
for i in range(0,11):
    if i == 5:
        continue
    print(i)
# print only pair numbers between 0-10
print("====================================")
for i in range(0,11):
    if i % 2 == 1:
        continue
    print(i)

# pass is used to do nothing
print("====================================")
for i in range(0,11):
    if i % 2 == 1:
        pass
    else:
        print(i)
print("====================================")
# Nested loops

for x in range (2):
    for y in range(3):
        print(f"x={x}, y={y}")

print("====================================")
data = [[1,5],[2,7],[3,3]]

for elem in data:
    for xy in elem:
        print(xy)
print("====================================")

i = 0
x = 0
while i < 5:
    print(f"i is {i}")
    while x < 10:
        print(f"x is {x}")
        x = x+1
    i += 1
print("====================================")
startdate = datetime.now()
while True:
    current_time_str = datetime.now().strftime("%H:%M:%S") # get the current time then convert it to string
    print(current_time_str)
    time.sleep(1) # wait 1 second
    if datetime.now() - startdate >= timedelta(seconds=10): # if delta time is greater than or equal to 10 seconds
        break # exit while loop

# looping over Dictionaries

person = {"name": "Sam", "age": 30}

for key,value in person.items():
    print(key, "=>", value)

for key in person.keys():
    print(key, "=>",person[key])

# looping over strings

mystring = "Hello World !"
newstring = ""
for char in mystring:
    if char == "l":
        newstring += "m"
    else:
        newstring += char
print(newstring)
print("====================================")
"""
Problem:
Print numbers from 1 to 20.
Print "Fizz" for multiples of 3.
Print "Buzz" for multiples of 5.
Print "FizzBuzz" for multiples of both.

"""
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)