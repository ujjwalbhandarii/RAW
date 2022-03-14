# faulty calculator

# design a calculator which will solve all the problems except
# 45 *3 = 555, 56 + 9 = 77 ,  56/6 =4

ope = int(input("Choose number according to operator:\n1. +\n2. -\n3. *\n4. /\n"))
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))


if(ope == 1):
    if(a == 56):
        if(b == 9):
            print("77")
        else:
            print(a+b)
    else:
        print(a+b)

elif(ope == 2):
    print(a-b)

elif(ope == 3):
    if(a == 45):
        if(b == 3):
            print("555")
        else:
            print(a*b)
    else:
        print(a*b)

elif(ope == 4):
    if(a == 56):
        if(b == 6):
            print("4")
        else:
            print(a/b)
    else:
        print(a/b)
