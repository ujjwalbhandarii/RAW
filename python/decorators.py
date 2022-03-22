# examples of decorators


# basic of how function works
def fun1():
    print("this is return function")
fun2 = fun1
del fun1
fun2()
print()


# function can also return function { here sum and print are build in functions }
def fun3(x):
    if x==0:
        return sum
    if x==1:
        return print
print(fun3(0))
print(fun3(1))
print()


# function can also be passed as a argument
def farg(fun1):
    def farg2():
        print("executing now")
        fun1()
        print("executed")
    return farg2

def decoratorF():
    print("hy there form decoratorF")

decoratorF = farg(decoratorF)
decoratorF()
print()



# using of decorator with @function_name 
def farg(fun1):
    def farg2():
        print("executing now")
        fun1()
        print("executed")
    return farg2

@farg
def decoratorF():
    print("hy there form decoratorF")

# decoratorF = farg(decoratorF)     # --> @farg is used instead of this function
decoratorF()
print()
# works same as above function