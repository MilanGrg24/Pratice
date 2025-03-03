#Number guessing game

#Simply making it using while loop and if-else condition

# print()
# print("Welcome to the number guessing game.\n")
# print("I'm thinking of a number between 1 and 100.\n")
# print("You have to guess the number.\n")

# while True:
#     #Taking numbers from user
#     guess = int(input("Guess the number to win the game: "))
#     #if the guessed number is correct the loop will break
#     if guess == 45:
#         print("Congratulations, you won the game.\n")
#         break
#     #if the given number is higher than the correct number print this
#     elif guess > 45:
#         print("Sorry, the number is lower than your guess number.\n")
#     #if the given number is higher than the correct number print this
#     elif guess < 45:
#         print("Sorry, the number is higher than your guess number.\n")


#Now by using RANDOM module

#importing random module
import random

#from random module I am using randint
number = random.randint(1,100)

print()
print("Welcome to the number guessing game.\n")
print("I'm thinking of a number between 1 and 100.\n")
print("You have to guess the number.\n")

while True:
    #Taking numbers from user
    guess = int(input("Guess the number to win the game: "))
    #if the guessed number is correct the loop will break
    if guess == number:
        print("Congratulations, you won the game.\n")
        break
    #if the given number is higher than the correct number print this
    elif guess > number:
        print("Sorry, the number is lower than your guess number.\n")
    #if th given number is lower than the correct number print this
    elif guess < number:
        print("Sorry, the number is higher than your guess number.\n")
