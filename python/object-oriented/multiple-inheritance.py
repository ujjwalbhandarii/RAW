
class Employee:
    NoOfLeaves = 10
    var = 8
    def __init__(self,aname,aage,alanguage) -> None:
        self.name = aname
        self.age = aage
        self.language = alanguage

    def printDetails(self):
        return f"{self.name} {self.age} {self.language}"

class Player:
    var = 9
    def __init__(self,aname,games,awin) -> None:
        self.name = aname
        self.game = games
        self.win = awin

class Programmer(Employee, Player):
    pass

# making object 
ankit = Employee("ujjwal1",19,"nepali1")
prabesh = Player("ujjwal2",19,"nepali2")
ujjwal = Programmer("ujjwal3",19,"nepali3")

a= ujjwal.printDetails()      # for printing details of ujjwal object inherited from Employee class
print(a)

print(ujjwal.var)   # prints 8 because the 1st class passed at programmer class is Employee