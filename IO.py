# IO
""""
" r " --  reading mode    # defualt mode
" w " --  writing mode    # defualt mode 
" x " --  create file if not exist
" a " --  append, add content to a file
" t " --  text mode, 
" b " --  binary mode
" + " --  read + write

"""

# to open file
f = open("sensativeInfo.txt")
content = f.read()
print(content)

f.close()

# can also do
a = open("sensativeInfo.txt", "r")      # another argument was for reading. it exceptional as it is defualt
content = a.read()     # if we pass any value in the read( int ) then it will understand as length as count upto ( int )
print(content)

a.close()

# for reading line by line

b = open("sensativeInfo.txt", "r")
content = b.read()

for line in content:
    print(line)

# using readline fuction 

c = open("sensativeInfo.txt","r")

print(c.readline())  # only prints one line


# store lines in list 

e = open("sensativeInfo.txt", "r")
print(e.readlines())   # this will print lines in the form of list