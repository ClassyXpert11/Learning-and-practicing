import random

in_game_currency = [1000, 1500, 2000, 2500]
health = [20, 30, 40]
bandages = ["Small bandage", "Medium bandage", "Large bandage"]
trunk = ["in_game_currency", "health", "bandages"]
player_money = 0
player_health = 75
player_bandages = 0

trunk_choice = random.choice(trunk)
#trunk_choice is the variable that is used to get a random item from the trunk variable
print(trunk_choice)

if trunk_choice == "in_game_currency":
  #this is if the in_game_currency gets selected then this code below will run
  currency_choice = random.choice(in_game_currency)
  #the currency_choice is variable that is used to pick something random from within the in_game_currency variable
  player_money += currency_choice
  #this adds whatever number came out of currency_choice to player_money
  print(player_money)
  #this will print when there is something to add with the above code

if trunk_choice == "health":
  health_choice = random.choice(health)
  player_health += health_choice
  if player_health > 100:

 if trunk_choice == "bandages":
  bandages_choice = random.choice(bandages)
  player_bandages + bandages_choice
  print()

