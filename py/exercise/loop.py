# Quiz
# make a list first -- can have anything
# detect if its a number
# if yes then, print number which is greater than 6


quizList = ["ujjwal", 12, 13, "ankit",
            "prabesh", "haridas", 13333, 8, 9, 10000, 5]

for i in quizList:
    # isnumeric() is used to check if string is numeric or not
    if str(i).isnumeric() and i > 6:
        print(i)
