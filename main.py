import random
from replit import clear
from art import logo
r
""" Funtion that generates a random number"""

""" Funtion the used to chose level and how much chances the player receive"""
def level(Level_choose):
  if Level_choose == "easy":
    return 10
  elif Level_choose == "hard":
    return 5

def compare(random_number, guessed_number):
  if random_number == guessed_number:
    return 0
  elif random_number < guessed_number:
    return 1
  elif random_number > guessed_number:
    return 2

def guess_number_game():
  print(logo)
  ran_number = random.randint(1, 100)
  print("Welcome to the Number Guessing!")
  print("I'm Thinking of a number between 1 and 100.")
  print(f"The answer is {ran_number}")
  level_choose = input("Choose a different. Type 'easy' or 'hard': ")

  attempts = level(level_choose)

  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess_number= int(input("Make a guess: "))
    does_it_match=compare(ran_number, guess_number)
    if does_it_match == 0:
      attempts = 0
      print("you won")
    elif does_it_match == 1:
      attempts -= 1
      print("to high")
    elif does_it_match == 2:
      attempts -= 1
      print("to low")
    if does_it_match == 2 or does_it_match == 1 and attempts !=0:
      print("try again")

  print(f"game over the number was {ran_number}")

while input("Do you want to play a game of Guess the Number ? Type 'y' or 'n': ").lower() == 'y':
  clear()
  guess_number_game()