# short shands

# printing number from 1 - 10 
newlist = [print(x, end=" ") for x in range(10)]
print("\n")

# anther
x = [print(x+1) for x in range(10)]
print()

# another
a = [print(x) for x in range(10) if x>5]
print()

# printing list in one line
fruits = ["apple",'ball','mango','pinapple','ujjwal','hari','wter']
[print(i) for i in fruits]
print()


# prints the list item which has only "a" alphabet
newList1 = [i for i in fruits if "a" in i ]
print(newList1)
print()

# using upper funtion
fruits = ["apple",'ball','mango','pinapple','ujjwal','hari','wter']
aplle = [x.upper() for x in fruits]
print(aplle)
print()

# using if else in list in shorthand
fruits = ["apple",'ball','mango','pinapple','ujjwal','hari','wter', 'banana']
new = [x if x!= "banana" else "orange" for x in fruits]
print(new)
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".