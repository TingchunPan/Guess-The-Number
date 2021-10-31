#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from random import randint


EASY_TURNS=10
DIFFICULT_TURNS=5

def set_difficulty():  
  choice=input("Choose a difficulty. \nType 'easy' or 'hard': ")
  if choice=='easy':
    return EASY_TURNS
  elif choice=='hard':
    return DIFFICULT_TURNS
  
def guess(newGuess, correct_number,turns):
  if newGuess>correct_number:
    print("Too high.")
    return turns -1
  elif newGuess<correct_number:
    print("Too low.")
    return turns -1
  else:
    print(f"You get the anwser {correct_number}.")

def game():

  correct_number=randint(1, 100)
  print(logo)
  print("Welcome to the Guess The Number Game.\nI'm thinking of a number between 1 and 100.")
  #print(f"The correct number is {correct_number}")

  turns=set_difficulty()

  newGuess=0
  while newGuess != correct_number:
   print(f'You have {turns} attempts remaining to guess the number.')
   newGuess=int(input("Please guess the number. "))
   turns=guess(newGuess, correct_number,turns)
   if turns==0:
     print("You've run out of guesses, you lose.")
     return
   elif newGuess != correct_number:
     print('Guess again.')

game()





  


