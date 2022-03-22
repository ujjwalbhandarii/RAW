

# string formatting
l = "ujjwal"
a = "this is %s" %l    
print(a)


# another 
n = 3
a2 = "this is %s %s"%(l,n)   # passed tuple
print(a2)

# best way -- using format()

a3 = "this is {} {}"
b = a3.format(l,n)
print(b)



# f string syntax
# a = f"this is string"    --> this means this is a f string
a4 = f"this is {n} {l}"
print(a4)


a5 = f"this is {n} {l} {2*2}"
print(a5)




import math

a5 = f"this is {n} {l} {math.cos(65)}"  
print(a5)

