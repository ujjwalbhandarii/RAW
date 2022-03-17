
# In Python programming, an anonymous function or lambda expression is a function definition 
# that is not bound to an identifier (def).  "lambda" opeartor is used for it


# example of lamda 
someNum = lambda a, b, c : a + b + c;
print("result is",someNum(10,10,10))


next = lambda na,pa, pap : na*pa*pap
print("result is",next(1,1,2))


# We can create anonymous functions wherever they are needed. Due to this reason, Python Lambda Functions 
# are also called as throw-away functions which are used along with other predefined functions 
# such as reduce(), filter(), and map(). 


# using sort() with lambda


# SYNTAX
#lambda_function_name = lambda "arg": "statement"
f_name = lambda list: list[1]  # this is lambda function

# GENERAL FUNCTION
# def f_name(list):
#     return list[1]

list = [ [ 10 , 20 ] , [ 2 , 3 ] , [ 4 , 5 ]]
list.sort(key=f_name)    # key is an argument that takes function as input.
print(list) 
# this will sort all the list inside list in increasing order



# program to sort list item 
fun = lambda mylist: mylist

mylist = [1, 100, 99, 18]
mylist.sort(key=fun)
print(mylist)