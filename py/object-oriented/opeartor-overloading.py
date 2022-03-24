
# dunder methods --> starts with __ and ends with __

class Employee:
    def __init__(self,aname,aage,asalary) -> None:
        self.name = aname
        self.age = aage
        self.salary = asalary
    
    def printInfo(self):
        return f"{self.name}, {self.age}, {self.salary} "
    
    # operator overloading
    def __add__(self,other):   # special method --> dunder method
        return self.salary + other.salary

    def __repr__(self) -> str:
        return self.printInfo()

    def __str__(self) -> str:
        return f"{self.name}, and age is {self.age}, and salary is {self.salary} "
        

# instances
ujjwal = Employee("ujjwal",12,13)
bhandari = Employee("ujjwal",12,13)
print(ujjwal + bhandari)  # works and prints the add of salary of ujjwal and bhandari object

#for repr and str
print(ujjwal)   # str is priorty
print()

# individual
print(str(ujjwal))
print(repr(ujjwal))

