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






# writing in a file 
f = open("ujjwal.txt","w")   
f.write("ujjwal is a cool boy")

f.close()


# writing in appending mode
f = open("ujjwal.txt","a")  # this will add the .write("content") in the file except erasing all
f.write("ujjwal is a cool boy")

f.close()

# characters written in a file
f = open("ujjwal.txt","a")
abc = f.write("this content will be added")

print(a)
f.close()


# from user input
f = open("ujjwal.txt","a")
content = input("enter the text to write in the file\n")   # taking user input to write in a file
abc = f.write(content)   

print(abc)    # this will read the character length
f.close()


# handel read and write both   -- r+
f = open("sensativeInfo.txt","r+")

print(f.read()) # this will read from file and print in terminal
f.write("\nthis content will be added")   # this will write agian


f.close()