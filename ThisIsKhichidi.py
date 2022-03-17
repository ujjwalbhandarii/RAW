

for x in "banana":
    print(x)

x = "this is me ujjwal"
print("is " in x)   # returns true
if "ujjwal" in x:
    print("wah! he is here")

print("he" not in x)




# using split 
a = "ujjwal bhandari"
print(a.split(" "))  # split function returns the list




# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

rollNo = 35
msg = "his roll no is {}"
print(msg.format(rollNo))


price = 36
msgg = "his name is ujjwal and his roll no is {2} but his age is {0} and another fact is his copy price is {1}"
print(msgg.format(age, price , rollNo))






# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
thisIsList = ("ujjwal","sid","ankit","prabesh")
print(list(thisIsList))




# changing list item value
thisList = ["ujjwal","bhandari","ankit"]
thisList[1] = "anu"

print(thisList)




# change item from the list , ramge of numbers
thisRangeList = ["prabesh", "ujjjwal","ankit","sid","ujjwal","anushka"]
thisRangeList[1:3] = ["elephent","ant"]    # two value will be changed "ujjwal", "ankit"
print(thisRangeList)


# Change the second value by replacing it with two new values:
anotherList = ["ujjwal","ankit","anu"]
anotherList[1:2] = ["change1","changed2"]
print(anotherList)


print() # for spacing



# insert() function
myList = ["ujjwal","ankit",1999]
myList.insert(2,"anu")           # 2 represent index where anu will be placed 
print(myList)  



myList = ["ujjwal","ankit",1999]
myList.append("anu")           # push to the last
print(myList)  


# To append elements from another list to the current list, use the extend() method.
myList1 = ["ujjwal","is","my","name"]
msg = ["anu","bhandari","name","2"]
myList1.extend(msg)
print(myList1)


# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
noramalList = ["ujwal","anu","bhandari"]
myTuple = ("199","1444$")
noramalList.extend(myTuple)
print(noramalList)


# using pop()
popElement = ["ujjwal","banana","ankit"]
popElement.pop(1)    # can only take integer # 0 - ujjwal, 1 - banana, 2 - ankit 
print(popElement)


# del keyword 
list9 = ["apple","anu","chuppa"]
del list9[2]
print(list9)