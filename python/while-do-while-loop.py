# while -- break -- continue

""""
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.

Example
Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1


The break Statement
With the break statement we can stop the loop even if the while condition is true:

Example
Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:

Example
Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



The else Statement
With the else statement we can run a block of code once when the condition no longer is true:

Example
Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


"""
# exmaple of while loop
i = 0

while(i < 45):
    print(i)
    i += 1


# break
while(True):
    print(i+1, end=" ")
    i += 1
    if i == 50:
        break


# continue statement
while(True):

    if (i+1) < 5:
        i += 1
        continue

    if i == 50:
        # i += 1
        break

    print(i+1, end=" ")
    i += 1
