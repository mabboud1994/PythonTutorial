# Creating a Dictionary
my_dict = {"name": "mahmoud", "age": 31, "city": "Rennes"}
print(my_dict)
 # Accessing Values
name = my_dict["name"] # You can access the values using the keys, raises an exception if key does not exist

name = my_dict.get("test") # same, but if key does not exist, then it returns None instead of raising an exeception
print(name)

#Adding or Updating Keys and Values
my_dict["skill"] = 10 # if key does not exist, the key value pair will be added
print(my_dict)

my_dict["skill"] = 15 # if key exists, then the value will be updated.
print(my_dict)

# Deleting Keys

del my_dict["skill"] # direct access to key in my_dict (no copy modified)
print(my_dict)

updated_dict = my_dict.pop("name") # same direct access, but it returns the value of the deleted key
print(updated_dict)
print(my_dict)

my_dict.popitem() # removes last item
print(my_dict)

# Getting Keys, Values, and Items
myKeys = my_dict.keys() # return a dict_keys type which can be casted to list
print(list(myKeys)) # cast to list

myValue = my_dict.values() # return a dict_values type which can be casted to list
print(list(myValue)) # cast to list

# get items
items = my_dict.items() # can be casted to list
myListofItems = list(items) # cast to list
print(myListofItems) # is a list of tuple
print(type(myListofItems[0]))
print(myListofItems[0][0]) # first element of list -> first element of tuple

# Dictionaries can also contain other dictionaries or lists.

person = {
    "name": "Alice",
    "contacts": {
        "email": "example.com",
        "phone": "075646464",
        "address": {
            "rue": "8 sq",
            "postal Code": 35000
        }
    },
    "lastSeen": [10,15,20]
}
# Accessing nested dictionary values
print(person["contacts"]["email"])
print(person["contacts"]["address"]["rue"])
print(person["lastSeen"][0]) # first item of list

#Merging Two Dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
#dict1.update(dict2) # Using update method
#print(dict1)

# Using ** unpacking operator

merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}



# Copying a Dictionary

new_dict = my_dict.copy()
print(new_dict)

#Clearing a Dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# create a dictionnary from string
new_dict = my_dict.fromkeys("mahmoud")
new_dict["m"] = 10
print(new_dict)
