#Number guesing
import random
hidden = random.randrange(1,10)
hidden= 5
print("your clue is number is between 1 to 10")
guess= int(input("enter the guess:"))

if guess == hidden:
     print("you won!")
else:
    print("you lost!")
