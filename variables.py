# variables  dataType  typeCasting

# variables
from os import times


var = "ujjwal is a good boy"  # string
var1 = 12   # integer
var2 = 11.2  # floating number
var3 = False
var4 = "string concatinate"
print(" ")                   # This will reserve 1 line for us
print(var, var1, var2, var3)

# using type function
print(" ")
print(type(var))
print(type(var1))
print(type(var2))
print(type(var3))

# string concatination
print(" ")
# print(var + var1)  # only string can concatinate not string and int type.
print(var + " " + var4)

# type casting
"""
for type casting there are:
int()
str()
float()
"""
var5 = "12"
var6 = "13"
print(" ")
print(var5 + " " + var6)  # concatinate string but dont do addition
print(int(var5)+int(var6))       # converting string --> int type

# string( int(string) + int(string) ) --> output is stringss
print(str(int(var5)+int(var6)))


# To print hello world 10 times
print(" ")
print(var * 10)


# Taking input in python
print("Enter a number ")
num = input()   # variable_name = { input() }--input function
print(num)      # the num variable is a string type. so, we need to type cast before doing any mathmetical experiment with nums


# Quiz given from my python course video
# make a addition of two number from user input

print("Enter 1st number")
a = input()
print("Enter 2nd number")
b = input()
# converting into a int type because by defualt they are string type
print("Addition of two number is ", int(a)+int(b))
