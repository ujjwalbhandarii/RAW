#types of function 
# build in function 
# user defined function



# user defined function 

def fun():
    print("hy ujjwal")

fun() # function call

# function with params
def input(a, b):
    print("sum of two number is", a+b)

def average(a, b):      # function that finds average
    avg = (a+b)/2
    print("average is",avg)

def avg1(a,b):   # function with the return type
    svg = (a-b)/2
    return svg

input(2,3)
average(2,3)
v = avg1(14,3)
print("svg of two number is",v)        # to prevent none in output. we need to make it return type


# doc string 
 
def ujjwal():
    """this is for the demo of doc string. Till now, I'm using it as a comment but didn't know it is also called as doc string"""
    print("domo for doc string")

print(ujjwal.__doc__)   # this is how doc string is printed.     || IMPORTANT ||

