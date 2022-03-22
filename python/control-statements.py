# control statement
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

short hand ==>

if statement :
if a > b: print("a is greater than b")

else statement:
a = 2
b = 330
print("A") if a > b else print("B")

ternery operator or conditional operator
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

And
The and keyword is a logical operator, and is used to combine conditional statements:
Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

Or
The or keyword is a logical operator, and is used to combine conditional statements:
Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

Nested If
You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass
"""

var1 = 2
var2 = 3
# if else ladder
print("enter a variable")
var3 = int(input())
if (var1 > var2):
    print("var1 is greater")
elif (var3 > var2):
    print("var3 is greater")
else:
    print("var2 is greater")


# using if statement in list
mylist = [1, 2, 3, 4]
print(4 in mylist)     # checks and return value true or false
if 4 in mylist:       # 'in' keyword is used to check 4 is in mlist
    print("4 is in the list")

print(12 in mylist)  # returns false
print(12 not in mylist)  # returns true
if 12 not in mylist:
    print("12 is not in mylist")
print(" ")
