# loop quiz
# take input from user upto when its greater than 100

while(True):  # while True or 1 (same)
    num = int(input("enter a number: "))
    if(num == 101):
        print("you entered bigger number than hundred")
        break
    else:
        print("Tryagain !")
        continue
