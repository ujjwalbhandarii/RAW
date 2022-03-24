
# simple example of try and except in event handeling
a = input("enter a number: ")
b = input("enter another number: ")

try:
    print("sum of two number is",int(a)+int(b))

except Exception as e:    # as is a keyword
    print(e)

print("this line will be executed now")
