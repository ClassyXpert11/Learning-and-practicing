import random

#This is letting the user input any number from one to ten
#The int() before input() makes it so that it gets converted to a integar
random_user_number = int(input("Enter any number from 1 to 10: "))
print(random_user_number)

#This generates a random number between one and ten whilst including them
computer_random_number = random.randint(1, 10)
print(computer_random_number)

#This if statement check whether the user and the computer got the same number
#If they got the same number then it would print the first one
#If not then it would print the second one
if random_user_number == computer_random_number:
    print("We got the same number!")
else:
    print("We got different numbers...")


continue_number = input("Would you like to continue?: ")

while random_user_number != computer_random_number:
  if continue_number == "Yes":
    random_user_number = int(input("Enter any number from 1 to 10: "))
    print(random_user_number)
    computer_random_number = random.randint(1, 10)
    print(computer_random_number)
    if random_user_number == computer_random_number:
      print("We got the same number!")
    elif random_user_number != computer_random_number:
      print("We got different numbers...")
      continue_number = input("Would you like to continue?: ")
      print("Repeating")
    continue
  elif continue_number == "No":
    print("Ending")
    break