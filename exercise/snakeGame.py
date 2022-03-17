# snake water gun 
# 
import random 

print()
print("Snake | Water | Gun")
print()
chance = 0

while chance < 10:
    Rnum = random.randint(1,3)            # generating random number

    print("1. Snake\n2. Water\n3. Gun")
    choice = int(input("Your choice: "))

    if(choice == 1):
            # print("You are on 1")
            if(Rnum == 1):
                print("Is a tie match")
                chance = chance+1
                continue
            if(Rnum == 2):
                print("your snake loosed.\nYou Loose")
                chance = chance+1
                
                continue
            if(Rnum == 3):
                print("Gun killed your snake.\nYou Loose")
                chance = chance+1
                
                continue
            
    elif(choice == 2):
            # print("You are on 2")
            if(Rnum == 1):
                print("You Win. \nSake downed")
                chance=chance+1
                continue
            if(Rnum == 2):
                print("This is tie")
                chance=chance+1
                continue
            if(Rnum == 3):
                print("Gun get into water.\nYou win")
                chance=chance+1
                continue
        


    elif(choice == 3):
            print("You are on 3")
            # print("You are on 2")
            if(Rnum == 1):
                print("You Win. \nYou killed snake")
                chance=chance+1
                continue
            if(Rnum == 2):
                print("You loose.\nGun downed in water")
                chance=chance+1
                continue
            if(Rnum == 3):
                print("This is a tie match")
                chance=chance+1
                continue


    else:
            print("Invalid input")