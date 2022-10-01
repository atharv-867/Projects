# import random

# def randNo():
#     num=random.randint(1,20)
#     return num

# rmdnum=randNo()
# count=1
# print(rmdnum)
# Unum=int(input("Guess the no. from 1-20: "))
# while Unum!=rmdnum:
#     if(Unum>rmdnum):
#         print(f"Your guess-{Unum}--> GUESS LOWER")
#         count+=1
#         Unum=int(input("Try again- "))
#         continue
#     elif(Unum<rmdnum):
#         print(f"Your guess-{Unum}--> GUESS HIGHER")
#         count+=1
#         Unum=int(input("Try again- "))
#         continue

# print(f"your guess-{Unum} Actual no.-{rmdnum}-->The perfect guess")
# print(f"You tried {count}times")

import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
