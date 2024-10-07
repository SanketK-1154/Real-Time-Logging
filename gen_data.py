import random
import string
import time
num = str(random.random())
seq = 0

for i in range(100) :
    file = open("my.log", 'a')
    time.sleep(1)
    file.write(str(seq) + ": " + str(random.random()) + str(random.random()) + str(random.random())  + '\n')
    if seq == 100:
        seq = 0
    else:
        seq = seq + 1
    #file.close()

