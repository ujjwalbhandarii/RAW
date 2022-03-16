# pattern problem


num = int(input("Enter the number: "))
print("PRESS")
decide = int(input("1. Upper Triangle\n0. Lower Triangle\n"))

new = bool(decide)

if new == True:
    # print("you entered 1")
    for i in range(num):
        for j in range(i+1):
            print("# ", end="")
        print()
                    
elif new == False:
    # print("you are in 2")
    for i in range(num):
        for j in range(num-i):
            print("# ", end="")
        print()

else:
        print("invalid!!")
