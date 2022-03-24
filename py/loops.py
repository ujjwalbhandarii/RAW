""""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator 
method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.



Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)




Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:
Loop through the letters in the word "banana":

for x in "banana":
  print(x)




The break Statement
With the break statement we can stop the loop before it has looped through all the items:
Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break




The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:
Example
Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)




The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.
Example
Using the range() function:

for x in range(6):
  print(x)



Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

Example
Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")





Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":

Example
Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)




The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

Example
for x in [0, 1, 2]:
  pass
"""

# for loop example
list = ["ujjwal", "hari", 'shyam', 'anushka', 'prabesh', 'ankit', 'sid']

for x in list:     # " x " is a user variable and can be replace by anyname
    print(x)


# for loop for list inside list
main = [["ujjwal", 2], ["sid", 3], ["prabesh", 4],
        ["ankit", 5]]  # list inside list

for i in main:
    print(i)     # prints the inside list

print(" ")
for i, y in main:
    print(i, y)  # prints inside list

print(" ")
for i, y in main:
    print(i, "eats ", y, "lolippop")


dict = dict(main)  # type casting
print(type(dict))  # type casting list into dict
print(dict)

print(" ")
for i, y in dict.items():   # item function is used to loop with dictinary
    print(i, y)

# if in only need of key in dictinary
print(" ")
for i in dict:
    print(i)
