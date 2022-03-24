''''
Introspection is an ability to determine the type of an object at runtime. Everything in python is an object. 
Every object in Python may have attributes and methods. By using introspection, we can dynamically examine python objects. 
Code Introspection is used for examining the classes, methods, objects, modules, 
keywords and get information about them so that we can utilize it. 
Introspection reveals useful information about your program’s objects. 
Python, being a dynamic, object-oriented programming language, provides tremendous introspection support. 
Python’s support for introspection runs deep and wide throughout the language.
Python provides some built-in functions that are used for code introspection.They are:

'''
# 1.type() : This function returns the type of an object.
# Python program showing
# a use of type function

import math

# print type of math
print(type(math))

# print type of 1
print(type(1))

# print type of "1"
print(type("1"))

# print type of rk
rk = [1, 2, 3, 4, 5, "radha"]

print(type(rk))
print(type(rk[1]))
print(type(rk[5]))
print()


# 2.dir() :This function return list of methods and attributes associated with that object.

# Python program showing
# a use of dir() function

rk = [1, 2, 3, 4, 5]

# print methods and attributes of rk
print(dir(rk))
rk = (1, 2, 3, 4, 5)

# print methods and attributes of rk
print(dir(rk))
rk = {1, 2, 3, 4, 5}

print(dir(rk))
print(dir(math))
print()


# 3.str() :This function converts everything into a string .

# Python program showing
# a use of str() function

a = 1
print(type(a))

# converting integer
# into string
a = str(a)
print(type(a))

s = [1, 2, 3, 4, 5]
print(type(s))

# converting list
# into string
s = str(s)
print(type(s))
print()


# 4.id() :This function returns a special id of an object.
# Python program showing
# a use of id() function

a = [1, 2, 3, 4, 5]

# print id of a
print(id(a))
b = (1, 2, 3, 4, 5)

# print id of b
print(id(b))
c = {1, 2, 3, 4, 5}

# print id of c
print(id(c))
print(id(math))
