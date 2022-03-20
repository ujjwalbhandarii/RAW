# only c++ and python allow multiple inheritance

# diamond shape problem  -- maily occer because of multiple inheritance
# is the confusion in which which class should use which class method

class A:
    def meh(self):
        print("this is a method from class A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass


# instances
a = A()
b = B()
c = C()
d = D()


# printing

d.meh()  # this will print the class A method