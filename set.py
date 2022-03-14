# sets in python

from turtle import pensize


mySet = set()
print(type(mySet))      # set type


"""
Some set function 

add():	             Adds an element to the set
clear():	         Removes all the elements from the set
copy():	             Returns a copy of the set
difference():	     Returns a set containing the difference between two or more sets
difference_update(): Removes the items in this set that are also included in another, specified set
discard():	         Remove the specified item
intersection():    	 Returns a set, that is the intersection of two or more sets
intersection_update():	Removes the items in this set that are not present in other, specified set(s)
isdisjoint():	        Returns whether two sets have a intersection or not
issubset():	            Returns whether another set contains this set or not
issuperset():	        Returns whether this set contains another set or not
pop():	                Removes an element from the set
remove():	            Removes the specified element
symmetric_difference():	Returns a set with the symmetric differences of two sets
symmetric_difference_update():	inserts the symmetric differences from this set and another
union():	                    Return a set containing the union of sets
update():	                    Update the set with another set, or any other iterable

"""


# list inside set
mySet1 = set([1, 2, 3, 4])
print(mySet1)

# another
l = [1, 2, 3, 4]
mySet2 = set(l)
print(mySet2)


# adding elements in set
mySet.add(1)
mySet.add(1)
mySet.add(2)
print(mySet)  # set retains the unique value only so, 1 will be printed only once

# union function
setUnion = set({1, 2, 3})
s1 = setUnion.union({10, 11})
print(setUnion, s1)

# intersection function
s2 = setUnion.intersection({1, 2})
print(s2)

print(len(s2))
print(min(s2))
print(max(s2))
print(type(s2))


# disjoint function
s3 = {4, 6}
print(mySet.isdisjoint(s3))


# removing from set
print(mySet1)
mySet1.remove(2)
print(mySet1)
