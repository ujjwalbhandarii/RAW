# pattern problem
from pip import main


num = int(input("Enter the number: "))
decide = int(input("1. True\n2. False\n"))

if decide == 1:
    decide = "True"
    
elif decide == 2:
    decide = "False"

if decide == "True":
    print("you entered 1")
    for i in range(num):
        for j in range(i+1):
            print("# ", end="")
    print()
                    
elif decide == "False":
    print("you are in 2")
    for i in range(num):
        for j in range(num-i):
            print("# ", end="")
    print()

else:
        print("invalid!!")
