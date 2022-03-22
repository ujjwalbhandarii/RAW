# inheritance
class Employee:
  def __init__(self, UserName) -> None:
       self.name = UserName

  def printName(self):
      return f"this is returned from self and his name is {self.name}"

class Employee2(Employee):  # inheritance
  def s_print_name(self):
    return f"this is returned from 2nd self and his name is {self.name}"

# object
ujjwal = Employee("ujjwal")

# another class object
bhandari = Employee2("bhandari")

print(ujjwal.printName())
print(bhandari.s_print_name())

print()





# another example

class Employee4:
    no_of_party = 19
    def __init__( self, a_name, a_age, a_year ):
        self.name = a_name
        self.age = a_age
        self.year = a_year


class Employee2(Employee4):  # inheritance
    def printwork(self):
        return f"the emploee name is {self.name} and his age is {self.age} and he is this year {self.year} old"

# anu = Employee4("anu stha", 19, 1999)
# dilu = Employee4("dilu kumari",20, 1998)

# new objects
ujjwal = Employee2("ujjwal bhandari",21, 1000)

# anu.printDetail("ujjwal")
print(ujjwal.printwork())