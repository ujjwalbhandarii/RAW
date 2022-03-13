# String slicing and others

mystr = "Hello, I am Ujjwal"
print(mystr[1])  # prints "e"
print(len(mystr))   # len() -- is a function which gives the length of a string
print(mystr[0:1])   # [ from where : upto where ]
print(mystr[0:5:2])  # [ from where : upto where : gap ]


# how to revert string
str = "hello"
print(len(str))  # gives length
print(str[::-1])  # reverse the string


print(str.isalnum())  # returns ( True )      alpha numeric --> isalnum()
print(mystr.isalnum())  # returns ( false )  because it have gaps

print(str.isalpha())  # returns true
print(str.endswith("hello"))  # returns true --> its is ending with "true"
print(str.endswith("bdy"))  # returns false because it is not ending with bdy

print(str.count("l"))  # counts the number of " l " in the string
print(str.capitalize())  # capatilizes the first letter
print(mystr.find("am"))  # tells "am" is in 9th place in a string
print(mystr.lower())  # make string lower case
print(mystr.upper())  # convert the string to a upper case
print(mystr.replace("am", "aim"))   # replace("what to replace","replace text")
