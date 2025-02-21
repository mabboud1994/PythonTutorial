"""  List """

#append(): Adds an element to the end of the list.
my_list = [1,2,3]
my_list.append(4) # adds 4 at the end
print(my_list)

#insert(): Adds an element at a specific position (index).
my_list = ["a","b","c"]
my_list.insert(1, "d")
print(my_list)

#extend(): Adds elements from another iterable (like another list) to the end.
my_list = ["a","b","c"]
my_list.extend(["d", "e"])
print(my_list)

#remove(): Removes the first occurrence of a specific value.
my_list = ["a","b","c", "c", "c"]
my_list.remove("c")
print(my_list)

#pop(): Removes and returns an element at a given index (default is the last element).
my_list = ["a","b","c", "c", "c"]
my_removed_elem = my_list.pop(1)
print(my_removed_elem)
print(my_list)

my_list = ["a","b","c", "c", "c"]
my_removed_elem = my_list.pop()
print(my_removed_elem)
print(my_list)

#del: Deletes an element or the whole list.
my_list = ["a","b","c", "c", "c"]
del my_list[1] # removes elem at index 1
print(my_list)
del my_list # removes the whole list (del removes also the variable from memory)

#clear(): Removes all elements from the list.
my_list = ["a","b","c", "c", "c"] # clear does not delete the reference of the variable
my_list.clear()
print(my_list)

#sort(): Sorts the list in-place (modifies the list).
my_list = [3,1,4,2]
my_list.sort() # Sorts in ascending order
print(my_list)

my_list = ["c", "c", "c", "z", "a"]
my_list.sort() # Sorts in ascending alphabetic order
print(my_list)

my_list = ["c", "c", "c", "z", "a", 5,4]
#my_list.sort() # it raises an exception: not supported between instances of 'int' and 'str'
#print(my_list)

#sorted(): Returns a sorted copy of the list without modifying the original.
my_list = [3,1,4,2]
my_new_list = sorted(my_list) #  Returns a new sorted list
print(my_list)
print(my_new_list)

#Get a sublist from index start to end-1:
my_list = ["c", "c", "c", "z", "a", 5,4]
sublist = my_list[0:4] # right index is excluded
print(sublist)
sublist = my_list[:] # copy of the whole list
print(sublist)

#reverse(): Reverses the list in-place
my_list = [2,1,3, 4, 5]
my_list.reverse()
print(my_list)

# count() return num of occurences of an item in a list
my_list = [1, 2, 3, 4, 5, 5,5]
print(my_list.count(5))

my_list = [1, 2, 3, 4, 5, 5,5]
print(my_list.index(5))

# copy() a lsit to another list
mycopiedList =  my_list.copy()
print(mycopiedList)

# List comprehensions allow you to create lists using a concise and readable syntax.

my_list = [1, 2, 3, 4]

squared_list = [x**2 for x in my_list]
print(squared_list)
# the same
squared_list = []
for i in my_list:
    squared_list.append(i**2)
print(squared_list)

my_list = [x for x in range(20,101)]
print(my_list)

# Concatenation of two or many lists
my_list1 = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]

myresult = my_list1 + my_list2
print(myresult)

"""  Sets """
#Creating a Set:
my_set = {1, 2, 3, 4} # declaration
my_set = set([1, 2, 3, 4]) # same

#Adding Elements: You can use the add() method to add a single element.
my_set.add(5)
my_set.add(5) # this will be ignored because 5 is already added by previous statement
print(my_set)

#Removing Elements: You can use remove() or discard(). remove() raises an error if the element is not found, while discard() doesn’t.

my_set.remove(4)  # Removes 4
my_set.discard(6)  # No error, since 6 is not in the set
print(my_set)

#Union: Combine two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

#Intersection: Get elements common to both sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)

#Difference: Get elements in set1 but not in set2.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(difference_set) 

#Symmetric Difference: Get elements that are in either set1 or set2, but not both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}

#Creating a Frozenset:
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4})
#No Adding or Removing: You cannot add or remove elements after the frozenset is created.
#my_frozenset.add(5) # will raise an exception

#Use in a Set or Dictionary: Because frozensets are immutable, they can be used as elements in a set or as keys in a dictionary.
dictionary = {frozenset([1, 2]): "value"}
print(dictionary)

"""   Exercise   """

"""
On a un website (API), qui possède une methode qui nous retourne les données des utilisateurs
authentifé et qui sont sotqué dans la base de données. un utilisateur est representé par 
son prenom, nom, adress, last connection, inventory

un user est representé par un dict:

le prenom, nom sont des string.
l'adress est un dict qui contient le mail, le numéro de rue, le code postal.
la last connection est une string.
l'inventory est un dict qui contient: le nombre de skins, le nom de companion, la liste des armes

on a fait un appel à cet API et il nous a retourné une liste de 3 users.

1- créer une list qui s'appel Users_list qui est empty à la déclaration
2- créer les dictUser1, dictUser2 et dictUser3 qui sont vide à la déclaration et qui representent conséquetivement ces 3 users.
3- definir 6 strings: (PrenomUser1, nomUser1, prenomUser2 etc..) donner ce qui tu veux comme valeurs 
4- definir 3 dicts: adreesUser1, adressUser2, adressUser3 (donner des valeurx aux clés (mail, numéro de rue, code postal)) 
5- Créer les strings lastConnectionUser1, lastConnectionUser2 et lastConnectionUser3, donne les valeurs qui te conviennent
6- créer le dict inventory pour chaque user: InvDict1, InvDict2, InvDict3 (vide à la déclaration)
7- créer les 3 listes des armes pour chaque user: armesListUser1, armesListUser2, armesListUser3 vide à la déclaration
8- créer les 6 variables: nbSkinsUser1, NameCompanionUser1, nbSkinsUser2 etc.. donner ce qui tu veux comme valeurs 
7- le user1 possède comme armes: m416 et m16, le user 2 possède: p90 et le user 3 possède: awm  et m24. utiliser la syntaxe qui sert à ajouter ces elements aux listes des armes
8- utiliser la syntaxe qui sert à ajouter les key value pairs pour le prenom, nom et last connection pour chaque user dict
9- utiliser la syntaxe qui sert à ajouter les key value pairs pour le nombre de skins, le nom de companion et la liste des armes  pour chaque user inv dict.
10- utiliser la syntaxe qui sert à ajouter les key value pairs pour l'inventory, pour chaque user dict.
11- utiliser la syntaxe qui sert à ajouter les 3 user dicts à la liste Users_list
12- utiliser la fonction print pour afficher la liste Users_list
13- utiliser la syntaxe qui sert à obtenir la liste des armes du premier element de la liste Users_list, (stocker cet element dans une variable nommé outputList) 
14- utiliser la syntaxe qui sert à obtenir le premier element de la liste outputList (stocker cet element dans une variable nommé firstElem) 
15- utiliser la syntaxe qui sert à covertir le contenu de firstElem en uppercase
16- on veut formatter l'output pour bien afficher la Users_list. defenir une string qui formatté qui possède la valeur suivante: la liste de users list est: <ici la valeur de Users_list>
17- utiliser print pour l'afficher.


"""
Users_list = []
dictUser1 = {}
dictUser2 = {}
dictUser3 = {}
PrenomUser1 = "mahmoud"
nomUser1 = "abboud"
PrenomUser2 = "ahmad"
nomUser2 = "abboud"
PrenomUser3 = "khaled"
nomUser3 = "abboud"

adreesUser1 = {"mail": "test", "numéro de rue": 5, "code postal":35200}
adreesUser2 = {"mail": "test", "numéro de rue": 5, "code postal":35200}
adreesUser3 = {"mail": "test", "numéro de rue": 5, "code postal":35200}

lastConnectionUser1 = "dfdf"
lastConnectionUser2 = "dfdf"
lastConnectionUser3 = "dfdf"

InvDict1 = {}
InvDict2 = {}
InvDict3 = {}

armesListUser1 = []
armesListUser2 = []
armesListUser3 = []

nbSkinsUser1 = 10
NameCompanionUser1 = "sdsd"
nbSkinsUser2 = 10
NameCompanionUser2 = "sdsd"
nbSkinsUser3 = 10
NameCompanionUser3 = "sdsd"

armesListUser1.append("m416")
armesListUser1.append("m16")

armesListUser2.append("p90")

armesListUser3.append("awm")
armesListUser3.append("m24")

dictUser1["nom"] = nomUser1
dictUser1["prenom"] = PrenomUser1
dictUser1["last connection"] = lastConnectionUser1

dictUser2["nom"] = nomUser2
dictUser2["prenom"] = PrenomUser2
dictUser2["last connection"] = lastConnectionUser2

dictUser3["nom"] = nomUser3
dictUser3["prenom"] = PrenomUser3
dictUser3["last connection"] = lastConnectionUser3

InvDict1["nbSkins"] = nbSkinsUser1
InvDict1["nameCompanion"] = NameCompanionUser1
InvDict1["armes"] = armesListUser1

InvDict2["nbSkins"] = nbSkinsUser2
InvDict2["nameCompanion"] = NameCompanionUser2
InvDict2["armes"] = armesListUser2

InvDict3["nbSkins"] = nbSkinsUser3
InvDict3["nameCompanion"] = NameCompanionUser3
InvDict3["armes"] = armesListUser3

dictUser1["inventory"] = InvDict1
dictUser2["inventory"] = InvDict2
dictUser3["inventory"] = InvDict3

Users_list.append(dictUser1)
Users_list.append(dictUser2)
Users_list.append(dictUser3)

print(Users_list)