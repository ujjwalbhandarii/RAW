# ----------challenge --------
# input human age
# if age is greater than 18 then print you can drive
# if less than 18 than print you cannot drive
# if equal to 18 than print we cannot decide

print("enter your age: ")
age = int(input())

if (age > 18):
    print("you are", age, "and can drive")

elif (age == 18):
    print("we need to think about it")

else:
    print("you are less than 18. so, you can't drive")
