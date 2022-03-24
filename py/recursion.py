# recursive -- using function inside function




# iterative approch to find factoial
def iFacto(n):
    
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("enter a number: "))
print(iFacto(number))





# recursive methood
def rFacto(n):

    if n == 0:
        return 1

    if n == 1:
        return 1
    else:
        return n * rFacto(n-1)

num = int(input("enter a number for recursive: "))
print(rFacto(num))
