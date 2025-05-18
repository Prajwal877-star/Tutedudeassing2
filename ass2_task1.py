#To take input user and check whether it is  even and odd
number = int(input('Enter a number:'))#input from the user
if number >= 0:

 if (number % 2 == 0):
    print(number ,'is an even number.')

 elif(number!=0):
    print(number,'is an odd number')
else:
    print(number,'is invalid type whole numbers only')
print('Thank you')
