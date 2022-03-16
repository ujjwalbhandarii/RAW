# patten printing

# # # #
# # # #
# # # #
# # # #

for i in range(4):      # column         # i value starts from 0 
    for j in range(4):  # row
        print("# ", end="")
    print()


print() # for spacing

# another type
# 
# #
# # #
# # # #

for i in range(4): # we need 4 colums so range is 4
    for j in range(i+1):
        print("# ", end="")
    print()


print()  # for spacing 



# another type
# # # #
# # #
# #
#

for i in range(4):  # columns
    for j in range(4-i):  # rows
        print("# ", end="")
    print()    # when j loop done his work this line will shift in another line

# this can also work
num = int(input("Enter the number: "))
for i in range(num,0,-1):
    for j in range(0,i-1):
        print("# ",end="")
    print()






print()  # for spacing




# another type

      #
    # #
  # # #
# # # #


for i in range(4):
    for j in range(i-4):
        print("# ", end="")
    print()


print()






