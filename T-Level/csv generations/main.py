import pandas as pd

grns = pd.read_csv("pokemon.csv")

user_gen = int(input("Enter a number between 1 - 6\n"))
# this is asking the user for a number between 1 and 6. user_gen is holding the number that has been inputted by the user. the \n just tells the computer to put this code in a new line so that it looks neater and is easier to read
while user_gen > 6  or user_gen < 1:
  # this is asking the user to give a number between 1 and 6 and won't accept anything higher or lower. if the user does give something higher or lower then they simply get asked again to put something between 1 and 6, repeatedly.
  user_gen = int(input("Enter a number between 1 - 6\n"))
else: 
  selected_gen = grns.loc[grns["Generation"] == user_gen]
# this prints out the generation that the user selected. selected_gen holds the output result of the entire generation selected by the user
  selected_gen.to_csv("Generation{}.csv".format(user_gen))
# this outputs the result into a csv file with the user's selected generation

