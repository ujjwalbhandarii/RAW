# no of gueses 9 
# print no of guesses left
# no of guesses he took to finish 
# game over

print("Find in 9 guesses only !")

noOfGuesses = 0

while noOfGuesses < 9:

    num = int(input("Enter a number: "))

    if(num == 18):
        print("WOW! you found a number and", 8 - noOfGuesses ,"guess still remain")
        break

    elif(num > 18):
        print("You have input larger number. You are very near to main number")
        noOfGuesses +=1
        print("guess left:", 9 - noOfGuesses)
        continue
        

    elif(num < 18):
        print("You have input smaller number. You are very near to main number")
        noOfGuesses +=1
        print("guess left:", 9 - noOfGuesses)
        continue


    else:
        print("Invalid Input")
        continue

if noOfGuesses == 9:
    print("\ngame over\n")