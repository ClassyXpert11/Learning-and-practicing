import random
import pandas as pd

player_score = 0
computer_score = 0
counter = 0
player_counter = 0
game_round = 0

options = ["rock", "paper", "scissors"]
name = input("Please enter your name: ")

print("###########################")
print(f"Welcome to the rock-paper-scissors game, {name}!\n")
print("###########################")

def asking():
  print("###########################")
  ask = input("Would you like to play 1,3 or 3 rounds?\nPlease enter 'one' for 1 round, 'three' for 3 rounds, 'five' for 5 rounds, 'seven' for 7 rounds and 'nine' for 9 rounds.\n")
  print("###########################")

  ask = ask.lower()
  if ask == "one":
    play_one_round()
  elif ask == "three":
    play_three_rounds()
  elif ask == "five":
    play_five_rounds()
  elif ask == "seven":
    play_seven_rounds()
  elif ask == "nine":
    play_nine_rounds()
  else:
    print("###########################")
    print("\nInvalid input. Please enter a round number!\n")
    print("###########################")
    asking()

def play_one_round():
  global counter, player_counter, game_round, player_score, computer_score
  player_counter = 1
  game_round = 0
  counter = 0
  player_score = 0
  computer_score = 0
  play()

def play_three_rounds():
  global counter, player_counter, game_round, player_score, computer_score
  player_counter = 3
  game_round = 0
  counter = 0
  player_score = 0
  computer_score = 0
  play()

def play_five_rounds():
  global counter, player_counter, game_round, player_score, computer_score
  player_counter = 5
  game_round = 0
  counter = 0
  player_score = 0
  computer_score = 0
  play()

def play_seven_rounds():
  global counter, player_counter, game_round, player_score, computer_score
  player_counter = 7
  game_round = 0
  counter = 0
  player_score = 0
  computer_score = 0
  play()

def play_nine_rounds():
  global counter, player_counter, game_round, player_score, computer_score
  player_counter = 9
  game_round = 0
  counter = 0
  player_score = 0
  computer_score = 0
  play()

def play():
  global player_score, computer_score, counter, player_counter, game_round
  computer = random.choice(options)
  counter += 1
  game_round += 1

  print("-------------------------------------")
  print(f"\nRound {game_round}!\n".upper())
  choice = input(f"Please enter your choice, {name}. Rock, paper or scissors?\n")
  
  if choice.lower() not in options:
    game_round -= 1
    counter -= 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nInvalid input. Please enter either 'rock', 'paper' or 'scissors'.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    play()
    return

  
  print(f"\nYou chose {choice.upper()}. The computer chose {computer.upper()}...\n")

  
  
  win_condition = {
    "rock" : "scissors",
    "paper" : "rock",
    "scissors" : "paper"
  }
    
  
  
  if win_condition[choice.lower()] == computer:
    print(f"\nYou WIN! Congratulations, {name}! ")
    player_score += 1
    print(f"The score is: {player_score} - {computer_score}. ({name} | computer)\n")
    print("-------------------------------------")
    if counter == 1 and player_counter == 1:
      play_again()
    elif counter == 3 and player_counter == 3:
      play_again()
    elif counter == 5 and player_counter == 5:
      play_again()
    else:
      play()
  elif choice.lower() == computer:
    print("\nIt's a TIE!")
    print(f"The score is: {player_score} - {computer_score}. ({name} | computer)\n")
    print("-------------------------------------")
    if counter == 1 and player_counter == 1:
      play_again()
    elif counter == 3 and player_counter == 3:
      play_again()
    elif counter == 5 and player_counter == 5:
      play_again()
    else:
      play()
  else:
    print(f"\nYou LOSE! Better luck next time, {name}!")
    computer_score += 1
    print(f"The score is: {player_score} - {computer_score}. ({name} | computer)\n")
    print("-------------------------------------")
    if counter == 1 and player_counter == 1:
      play_again()
    elif counter == 3 and player_counter == 3:
      play_again()
    elif counter == 5 and player_counter == 5:
      play_again()
    else:
      play()





