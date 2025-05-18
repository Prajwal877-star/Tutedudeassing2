#to write a program which will return the sum for 1 to 50

counter = 0
old = 0
serial = 1
for i in range(1,51):

     counter = serial + old
     old = counter
     serial +=1

print('The sum of the numbers from 1 to 50 :',counter)
