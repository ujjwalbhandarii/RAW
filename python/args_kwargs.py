
# ARGS
# def func( normal_arg, *args , **kwargs )
def func(*args):  # takes argument as a tuple           # args name can be name by any name
    print(args)
    print(type(args))

    # using for loop
    for x in args:
        print(x)

name = ["ujjwal","dilu","anu","asmit","aju"]
func(*name)


# using normal args and kwargs

def finc2(normal, *args1, **kwargs):
    print(normal)
    
    for j in args1:
        print(j)

    print("\nother members are : ")

    for k, value in kwargs.items():   # . items() function must be run it print dictinary
        print(f"{k} : {value}")

normal = "\nthis is normal argument"
dict = {"ujjwal":"anu","ujjwal":"aju","ujjwal":"asmit","ujjwal":"dilu"}

finc2(normal, *name, **dict)



print()
def func12(**kwing):
    for key, value in kwing.items():
        print(f"{key} : {value}")
    


# func12(**dict)




print()
# Python program to illustrate 
# *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        # print ("%s == %s" %(key, value))
        print(f"{key} : {value}")
 
# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks') 
