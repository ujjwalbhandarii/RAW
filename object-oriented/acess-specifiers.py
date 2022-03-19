

class Ujjwal:
    name = "ujjwal"    # public acess specifiers
    _age = 19          # this is a example of protected acess specifiers -- its starts from underscore
    __pvt = "this is priviate specifier"  # pvt specifiers start from double underscore ( __ )


myobj = Ujjwal()
print(myobj.name)
print(myobj._age)
print(myobj._Ujjwal__pvt)  # name mangeling { this is how to print priviate specifier }