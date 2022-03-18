class ujjwal:   # class
    pass

# making objects of class
hari = ujjwal()
anu = ujjwal()

print(anu)       # gives the memory location of a object 




# making instance variables
anu.name = "ujjwal bhandari"
anu.age = 19
anu.subjects = ["ujjwal","bhandari"]

print(anu.name)
print(anu.subjects)   # printing list
print()





# more on instance and class variables
class Employee: # classs
    no_of_leaves = 10
    pass

ujjwall = Employee()  # making object
ankitt = Employee()

ujjwall.name = "ujjwal bhandari"
ujjwall.age = 20
ujjwall.relationStatus = "Single"

print(f"my name is {ujjwall.name} and my age is {ujjwall.age} and i'm {ujjwall.relationStatus} but in his office he only get {ankitt.no_of_leaves} holiday ") # ujjwal.no_of_leaves is also possible


# we can change value of varible inside class by 
ujjwall.no_of_leaves = 1000 
print(ujjwall.no_of_leaves)
# but
print(Employee.no_of_leaves)  # will still remain 10 


print(ujjwall.__dict__)  # gives the dictinary of all the variables of ujjwal object instance
print(Employee.__dict__)