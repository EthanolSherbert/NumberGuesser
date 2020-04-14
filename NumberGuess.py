import random
import time
import sys

number = 0
guess = 0
score = 0
total_score = 0
right = 0
avg = 0

def Help():
    print("\n\nType a number between 0 and 100\n\nType 'help' to see a list of commands\n\nType 'end' to view your score and end the game\n\nType 'score' to view your score\n\n")

def Score():
    print("Score: ", total_score, "\nTotal right guesses: ", right, "\nAverage guesses per game: ", avg, "\n\n")

def End():
    Score()
    time.sleep(2)
    sys.exit(0)

Help()

while 1 == 1:
    number = random.randint(1,100)
    while 2 == 2:
        guess = input("Type a command or guess the number: \n\n")
        if guess == 'score':
            Score()
            time.sleep(1)
            continue
        elif guess == 'end':
            End()
            continue
        elif guess == 'help':
            Help()
            continue
        elif int(guess) < number:
            print("Too low!\n")
            score += 1
        elif int(guess) == number:
            print("You guessed the number!\n\n")
            score += 1
            total_score += score
            score = 0
            right += 1
            avg = (total_score / right)
            break
        elif int(guess) > number:
            print("Too high!\n")
            score += 1