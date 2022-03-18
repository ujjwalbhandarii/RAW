
# self 

class Ujjwal:
    no_of_lats = 8

    def myfun(self):   # self is the instance where the function is being implemented
        return f"Name is {self.name}. and his salary is {self.salary} "
        

ankit = Ujjwal()
sid = Ujjwal()

sid.name = "XYZ Bhandari"
ankit.name = "bhattaraiiii"

ankit.salary = 1000
sid.salary = 123

print(sid.myfun())
print()






# __init__ constructor
# constructor: giving argument to a class

class Employee2:
    def __init__(self,aname,asalary):  # constructors in python
        self.name = aname
        self.salary = asalary
        


ankit = Employee2("ujjwal bhandari",1200000)
print(ankit.name)
print()









# class methods

class Employee3:
    no_of_party = 19
    def __init__(self,a_name,a_age,a_year):
        name = a_name
        age = a_age
        year = a_year

    
    @classmethod             # using class methods
    def change_party(cls, party):
        cls.no_of_party = party
        


anu = Employee3("anu stha", 19, 1999)
dilu = Employee3("dilu kumari",20, 1998)

anu.change_party(101)
print(anu.no_of_party)
print()






# static methods
class Employee3:
    no_of_party = 19
    def __init__(self,a_name,a_age,a_year):
        name = a_name
        age = a_age
        year = a_year
    
    @classmethod             # using class methods
    def change_party(cls, party):
        cls.no_of_party = party
    
    @staticmethod           # using static method
    def printDetail(string):
        print("this is a string "+ string)
        


anu = Employee3("anu stha", 19, 1999)
dilu = Employee3("dilu kumari",20, 1998)

# anu.change_party(101)
# print(anu.no_of_party)

anu.printDetail("ujjwal")
