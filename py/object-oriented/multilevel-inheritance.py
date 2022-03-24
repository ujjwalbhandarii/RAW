# multilevel inheritance
class Dad:
    basketball = 5


class Son(Dad):
    sing = 2

    def cansing(self):
        return f"I can dance and i can also sing {self.sing} songs"


class Grandson(Son):
    sing = 7

    def cansing(self):
        return f"I can sing more good than my father. i know {self.sing} songs"


# making instances
sid = Dad()
ankit = Son()
ujjwal = Grandson()

# printing
# Son class function will be implemented if there is no cansing function in "Grandson" class
print(ujjwal.cansing())

print(ujjwal.basketball)  # prints 5
