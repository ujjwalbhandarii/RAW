# list dataType

# list are the list of anything. kinda same as array
from msilib.schema import TypeLib
from typing import Tuple

""""
SOME PYTHON LIST FUNCTION
sort(): Sorts the list in ascending order.
type(list): It returns the class type of an object.
append(): Adds one element to a list.
extend(): Adds multiple elements to a list.
index(): Returns the first appearance of a particular value.
max(list): It returns an item from the list with a max value.
min(list): It returns an item from the list with a min value.
len(list): It gives the overall length of the list.
clear(): Removes all the elements from the list.
insert(): Adds a component at the required position.
count(): Returns the number of elements with the required value.
pop(): Removes the element at the required position.
remove(): Removes the primary item with the desired value.
reverse(): Reverses the order of the list.
copy():  Returns a duplicate of the list.
"""

ujjwalNames = ["ram", "hari", "handsome", "hero", 14]  # this is a list
print(ujjwalNames)

# acessing items from list
print(ujjwalNames[1])  # prints "hari"

numList = [17, 12, 14, 15]
print(numList[1])  # gives 12

print(' ')
numList.sort()  # .sort() --> helps to sort or rearrange numbers
numList.reverse()  # makes list elements reverse
print(numList)


# list slicing
print(' ')
print(numList[:])  # takes defualt value i.e   [0:5]


# extended slice
print(" ")
print(numList)
print(numList[::-1])  # reverse the list

print(len(numList))  # prints 4
print(max(numList))  # gives the maximum valued number
print(min(numList))  # gives the minimun valued number


# append or add items it list   -- append adds numbers at last of list
numList.append(5)   # .append("param") --> add the number to the list
print(numList)


# insert   -- adds the number in a desire location in list
# numList( index , what number )
print(" ")
numList.insert(1, 1000)
print(numList)


# remove a number in a list
# remove(what number)
print(" ")
numList.remove(1000)
print(numList)


# pop --> pops or chopped the last digit
numList.pop()  # chopped the last digit
print(numList)


numList[1] = 19999
print(numList)
print(" ")


# --------------------- python tuple------------------------------------
# mutable Tuple   -- can change
# immutable tuple -- cannot change

# tuples are immuatble i.e. cannot be changed
tuple = (1, 2, 3)  # small brackets is used in tuple
print(tuple)

# swapping two numbers
a = 1
b = 2

"""
#Traditional way
temp = a
a = b
b = temp
print(a, b)
"""

# swapping using python
a, b = b, a   # for swapping a number
print(a, b)  # output will be 2 1
