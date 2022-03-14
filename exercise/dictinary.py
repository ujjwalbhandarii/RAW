# create a dictinary and take input from user and return the meaning from the dictinary
# input 5 words
# solved by selfs
myDic = {"hy": "greetings",
         "light": "that makes everything visible",
         'earth': 'where we live',
         'animals': 'creature of earth',
         'humans': 'more collectively known as human beings or homosapians'
         }
print(myDic.keys())   # for showing dictinary key items
print("Enter a word that you want to know meaning of ")
userInput = input()

print("Meaning of ", userInput, " is ", myDic[userInput])


# ------------other approches [ found in comments ]-----------------
usrInput = input("Enter a word to find it's meaning: ").capitalize()
d1 = {"Mutable": "Which can be changed",
      "Immutable": "Which Can't be Changed",
      "Abandon": "Complete lack of inhibition or restraint.",
      "Compunction": "A Feeling of guilt, distress or regret"
      }
print(d1.get(usrInput))
