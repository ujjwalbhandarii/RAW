# map function

Num = [ "1", "2", "3", "4" ]

for i in range( len(Num) ):
    Num[i] = int( Num[i] )

Num[2] += 1
print( Num[2] )



# above code can alse be performed using map function
Num = list(map( int, Num ))   # map function need to be type casted into list
print(Num[2]) 


# another
# def sq(x):
#     return x * x

sq = lambda x: x*x   # lambda function or anonyomus function
list1 = [2,3,4,5,6,20]
a = list(map( sq,list1 ))
print(a)


#another
print()

def square(x):
    return x*x

def cube(x):
    return x*x*x

func = [square, cube]

for i in range(5):
    abc = list(map(lambda x:x(i),func))
    print(abc)








# Filter function
print()
list1 = [2,3,4,5,6,20]

def is_greater_than_5(x):
    return x > 5

greater_than = list(filter(is_greater_than_5,list1))

print(greater_than)





print()
# reduce

# adding a list elements 
lis = [1,2,3,4]
num = 0
for i in lis:
    num = num + i
print(num)

# more efficient way to add using reduce()
from functools import reduce
lis12 = [1,2,3,4]
myf = lambda x,y:x+y
num = reduce(myf, lis12)
print(num)
# ImportError: cannot import name 'itemgetter' from 'operator' (d:\python\operator.py)
# while debugging it is working but not while compiling