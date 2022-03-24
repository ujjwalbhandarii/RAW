import time


# comparing which( while loop or for loop ) will run faster with the help of time module. 


intial = time.time()
# print(intial)
k = 1
while k <= 5:
    print("this is value of k", k)
    k += 1
print("time for while loop:", time.time() - intial)  # gives the time for while loop


intial2 = time.time()
for i in range(5):
     print("this is value of k", k)
print("time for for loop:", time.time() - intial2)  # gives the time for while loop



# this gives local time 
localTime = time.asctime(time.localtime(time.time()))
print(localTime)



# sleep function

s = "hello dilu"
for i in range(10):
    print(s)
    time.sleep(2)   # passed argument is in sec
    # this will stop the loop for 2 sec and continues back again after 2 sec