score = ""
import random

# User
choice = input("rock, paper, scissors, shoot: ")

if choice.lower() == "rock":
    move = 1
elif choice.lower() == "paper":
    move = 2
elif choice.lower() == "scissors":
    move = 3
else:
    print('error, undefined input')
    error
# IVA
numchoice = random.randint(1,3)
wordchoice = ""

if numchoice == 1:
    wordchoice = "rock"
if numchoice == 2:
    wordchoice = "paper"
if numchoice == 3:
    wordchoice = "scissors"

response = "You chose {0}, IVA chose {1}".format(choice, wordchoice)
print(response)


if move == numchoice:
    print("It was a tie.")
if move > numchoice:
    print("You won! :)")
if move < numchoice:
    print("You lost. :(")
