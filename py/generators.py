# Generator-Function :

# A generator-function is defined like a normal function,
# but whenever it needs to generate a value,
# it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.


'''
iterable  - __iter__() or __getitem__()
iterator  - __next__()
iteration - 

'''


def gen(n):
    for i in range(n):
        yield i


# g = gen(12316712871827178812)
g = gen(12)
print(g)
print(g.__next__())  # print 0
print(g.__next__())  # print 1
print(g.__next__())  # print 2
print(g.__next__())  # print 3
print(g.__next__())  # print 4
print()  # for new line


# A generator function that yields 1 for first time,
# 2 second time and 3 third time

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

print()  # for new line


"""
Generator-Object : 
Generator functions return a generator object. 
Generator objects are used either by calling the next method on the generator object or using the generator object 
in a “for in” loop
"""

# A Python program to demonstrate use of
# generator object with next()

# A generator function


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next
print(x.next())  # In Python 3, __next__()
print(x.next())
print(x.next())
print()

# As another example, below is a generator for Fibonacci Numbers.
# A simple generator for Fibonacci Numbers


def fib(limit):

    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.next())  # In Python 3, __next__()
print(x.next())
print(x.next())
print(x.next())
print(x.next())

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)


"""
Applications : 
Suppose we to create a stream of Fibonacci numbers, 
adopting the generator approach makes it trivial; we just have to call next(x) to get the next Fibonacci number 
without bothering about where or when the stream of numbers ends.
A more practical type of stream processing is handling large data files such as log files. 
Generators provide a space efficient method for such data processing as only parts of the file are handled 
at one given point in time. We can also use Iterators for these purposes, but Generator provides a quick way 
(We don’t need to write __next__ and __iter__ methods here).


"""
