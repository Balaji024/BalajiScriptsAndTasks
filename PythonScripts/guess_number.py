
import random
num= random.randint(1,10)
for guess in range (1,4):
     print ('I`ll give you three chances to find the number lets see ..!!! here we go')
     print ('Chance '+ str(guess))
     guess = int(input())
     if guess>num:
       print ('the number you guessed in bit high')
     elif guess<num:
       print ('the number you have guessed is bit low')
     elif guess == num:
       print('Wow you are awesome')
       break 
print ('thank you for playing the game with me see you again')
