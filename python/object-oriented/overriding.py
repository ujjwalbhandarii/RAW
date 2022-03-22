# using super and overriding

class A:
    classVarA = "Im a class varible of class A"

    def __init__(self) -> None:
        self.varA = "Im inside a constructor"
        self.classVarA = "Instance var in class A"  # this will be printed first constructor in outside variable

class B(A):   #inherited from class A
    classVarB = "Im a class variable of class B"
  
# instances

a = A()
b = B()

# printing
print(b.classVarA)
print()





# using super 

class A1:
    classVarA = "Im a class varible of class A"

    def __init__(self) -> None:
        self.varA = "Im inside a constructor"
        self.classVarA = "Instance var in class A"  # this will be printed first constructor in outside variable
        self.special = "special"

class B1(A1):   #inherited from class A
    classVarA = "Im a class variable of class B"

    def __init__(self) -> None:
        super().__init__()
        self.varA = "Im inside a constructor B"
        self.classVarA = "Instance var in class B"
        
        # super().__init__
        # print(super().classVarA)


# instances

a1 = A1()
b1 = B1()

# printing
print(b1.classVarA)
print(b1.special)
