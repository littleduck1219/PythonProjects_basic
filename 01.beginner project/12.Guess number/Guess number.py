from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def ckeck_guess(guess, answer, turns):
    if guess > answer:
      print("Too high")
      return turns -1
    elif guess < answer:
      print("Too low")
      return turns -1
    elif guess == answer:
      print(f"You got it! The answer was {answer}!")

      

def set_difficulty():
  level = input("Choose a difiiculty. Type 'easy' or 'hard' : ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  turns = set_difficulty()

  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))
    turns = ckeck_guess(guess, answer, turns)
    if turns == 0:
      print("You've run out of guess. you lose")
      return
    elif guess != answer:
      print("Guess again")
    
game()