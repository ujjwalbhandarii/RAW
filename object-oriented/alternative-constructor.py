
class Employee:
    def __init__(self,Uname,Uage,Ujob) -> None:
          self.name = Uname
          self.age = Uage
          self.job = Ujob
    
    def PrintDetails(self):
        return f"hello my name is {self.name}. I'm {self.age} years old and I'm a {self.job}"
    

    @classmethod
    def AlternativeConstructor(cls,string):
        myValue = string.split("-")
        # print(myValue)     # list will be printed
        return cls(myValue[0],myValue[1],myValue[2])        



# objects 
ujjwal = Employee("ujjwal bhandari",19,"programmer")
diluRam = Employee.AlternativeConstructor("DukhiRam-20-dukhi aatma")  # className.FunctionName(Params)  This should be followed
 
# printing details
print(ujjwal.PrintDetails())
print(diluRam.PrintDetails())
# print(diluRam.age)