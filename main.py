# imports
import os
import art
from game_data import data
import random

def clear():
  os.system("clear")

def format_option(option):
  return f"{option['name']}, a {option['description']}, from {option['country']}."

def check_answer(option1, option2, guess):
  answer = ""

  # check what the correct answer is
  if option1["follower_count"] > option2["follower_count"]:
    answer = "A"
  else:
    answer = "B"
  
  # check if the user's guess matches the correct answer
  if guess == answer:
    return True
  else:
    return False

def play_game():
  print(art.logo)

  option1 = random.choice(data)
  option2 = random.choice(data)
  
  continue_game = True
  score = 0
  while continue_game:
    option1 = option2
    option2 = random.choice(data)
    while option2 == option1:
      option2 = random.choice(data)

    print(f"Compare A: {format_option(option1)}\n{art.vs}\nAgainst B: {format_option(option2)}")

    user_choice = input("What has more followers? Type 'A' or 'B': ")
    clear()
    print(art.logo)

    is_correct = check_answer(option1, option2, user_choice)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      continue_game = False
      print(f"Sorry, that's wrong. Final score: {score}")
    
play_game()