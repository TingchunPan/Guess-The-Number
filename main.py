
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





  


