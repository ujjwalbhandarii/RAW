

list = ["gopi", "bhindi", "sabji", "aalu"]


# normal method
i = 1
# if need to get odd values only then 
for item in list:
    if i%2 is not 0:   # similar to !=
        print(f"items {i} is {item}")
    i+=1


print()
# using enumeration
for index, item in enumerate(list):
    if index%2 is 0:
        print(f"items {item} is {item}")



