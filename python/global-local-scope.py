# local scope global scope
# global keyword


# example of global and local scope [ nested function ]

a = 1  # global variable
def outer():
    b = 2
    print("Global is accssed here i.e",a,"and local is ",b)
    def inner():
        c = 3
        print("global var is",a,"outer local is",b,"and inner local is",c)
    
    inner()  # calling inside outer  
outer() # function call


print()




# example of global keyword

num = 12
def showc():
    global num
    num = 13

    print("global variable is changed with the help of global keyword inside function and it will only remain inside function scope. Changed value is", num)

print("value outside function",num)
showc() # function call


# global keyword in nested function
x = 1 
def fun1():
    x = 2
    
    def fun2():
        global x
        x = 3
        print("value of x inside nested funtion:", x)  # 3  -- inside nested funcion
    
    print("Value before calling fun2:",x)   #  2  -   before calling fun2() 

    fun2() # fun2 called

    print("Value after calling fun2:",x)  #  2  -   after calling fun2() 

print("value outside function:",x)  #  1  -   before calling fun1() 

fun1()

print("value after calling fun1:",x) #  3  -   after calling fun1() 
