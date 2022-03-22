# dictinary
# key value pairs

''''
SOME DICTINARY FUNCTION IN PYTHON ==>
clear():	Removes all the elements from the dictionary
copy():	Returns a copy of the dictionary
fromkeys():	Returns a dictionary with the specified keys and value
get():	Returns the value of the specified key
items()	:Returns a list containing a tuple for each key value pair
keys():	Returns a list containing the dictionary's keys
pop()	:Removes the element with the specified key
popitem()	:Removes the last inserted key-value pair
setdefault():	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update():	Updates the dictionary with the specified key-value pairs
values():	Returns a list of all the values in the dictionary

'''


d1 = {}  # blank dictinary
print(type(d1))

# dictinary are like objects of javascript. but denoted by curly braces '{ }'

dic = {
    "ujjwal": 12,
    "hari": 13,
    "shyam": 15
}
print(dic)  # prints the whole dictinary
# gives the other half i.e. 12      ----- It is case sensative
print(dic["hari"])

# dictinary inside dictinary
print(" ")
dic2 = {"ujjwal": "anu",
        "bhandari": "stha",
        "gyawali": {"bhattarai": "shyam",
                    "ujjwal": "bhandari",
                    "anushka": "sharma"
                    }
        }
print(dic2["gyawali"])  # prints the gyawali other half
print(dic2["gyawali"]["bhattarai"])   # prints shyam


# adding more on dic2
dic2["ankit"] = "naughty boy"  # adds the iteam at last
print(dic2)
dic2[680] = "jhukaga nahiii "
print(dic2)

# removing elements from dictinary
del(dic2[680])    # 680 element will be removed
print(dic2)


# Functions of dictinary

print(dic.copy())  # returns copy of dic dictinary

# for understanding
dic3 = dic
del(dic3["hari"])    # we have delected dic3 but value of dic is also changed
print(dic)


# for not having isses like this copy function is used
dic4 = dic.copy()
del(dic4["ujjwal"])
# ujjwal dont get delected as dic is a copy of original original dic
print(dic)

# using get funtion
dic5 = {"ujjwal": "bhandari", "siddhartha": "pandey",
        "ankit": "bhattarai", "prabass": "rayamajhi"}
print(dic5.get("ujjwal"))   # prints bhandari

# using update function
dic5.update({"yo update ho": "hello from update"})
print(dic5)


# using keys function
print(dic5.keys())   # prints the keys of all objects


# using item function
print(dic5.items())  # prints all key value pairs of dictinary
