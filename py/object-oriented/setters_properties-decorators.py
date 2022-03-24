from ast import Delete


class Employee:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"

    def explain(self):
        return f"My name is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


nepal_supporter = Employee("ujjwal", "Bhandari")


# print(nepal_supporter.email)

# if we try to change the email later like
# nepal_supporter.fname = "siddharth"
# this will not be changed because constructor had already taken the value at the run time.
# ujjwal.bhandari@gmail.com will be printed.
# print(nepal_supporter.email)

# this problem can be solved with the help of setter
# print(nepal_supporter.email())
# nepal_supporter.fname = "siddharth"
# print(nepal_supporter.email())


# after using @property
nepal_supporter.email = "this.that123@gmail.com"
print(nepal_supporter.email)

del nepal_supporter.email

print(nepal_supporter.email)
