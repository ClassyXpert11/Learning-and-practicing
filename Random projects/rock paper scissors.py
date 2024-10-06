import random

player_score = 0
computer_score = 0
counter = 0
player_counter = 0
game_round = 0

options = ["rock", "paper", "scissors"]
name = input("Please enter your name: ")
print("-------------------------------------")
print(f"\nWelcome to the rock-paper-scissors game, {name}!\n")
print("-------------------------------------")


def asking():
  print("-------------------------------------")
  ask = input("Would you like to play 1, 3 or 5 rounds?\nPlease enter 'one' for 1 round, 'three' for 3 rounds and 'five' for 5 rounds.\n")
  print("-------------------------------------")
  if ask.lower() == "one":
    play_one_round()
  elif ask.lower() == "three":
    play_three_rounds()
  elif ask.lower() == "five":
    play_five_rounds()
  else:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nInvalid input. Please enter the round number.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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



def play_again():
  global player_score, computer_score
  
  print("-------------------------------------")
  once_more = input("\nWould you like to play again? (yes/no)\n")
  print("-------------------------------------")

  
  if once_more.lower() == "yes":
    asking()
  elif once_more.lower() == "no":
    print("-------------------------------------")
    print(f"\nOh okay...\nGoodbye, {name}!\n")
    print("-------------------------------------")
  else:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nInvalid input. Please enter either 'yes' or 'no'.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    play_again()
    

asking()
