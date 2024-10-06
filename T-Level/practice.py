game_info = {"Uncharted 4" : {"release date" : 2016, "developer name" : "Naughty dog", "available on platforms" : ["PS4, PS5, PC"]}, "The Witcher 3" : {"release date" : 2015, "developer name" : "CD Projekt Red", "available on platforms" : ["PS4", "PS5", "PC", "Xbox one", "Xbox Series X/S"]}, "Devil May Cry 5" : {"release date" : 2019, "developer name" : ["Capcom U.S.A", "Capcom"], "available on platforms" : ["PS4", "PS5", "PC", "Xbox one", "Xbox Series X/S"]}}
# In this dictionary there is alot of information. However i want to print "PC", specifically from "The Witcher 3", "available on platforms".

print(game_info["The Witcher 3"]["available on platforms"][2])
# In order to grab "PC" from that specific list we have to go through "The Witcher 3" first then "available on platforms" then use indexing (because its a list) to finally grab "PC"

print(game_info["Uncharted 4"]["release date"])
# Here i am grabing "2016" from "Uncharted 4", "release date". Notice how we did not have to use indexing. This is because there is only one value from that specific nested key and it is not a list.

print(game_info["Devil May Cry 5"]["developer name"][1])
# Another note is that a dictionary key can have multiple values without a list however, if you want to obtain a specific value from that dictionary key you will have to use a list as it is not possible to obtain that value without it.

print(game_info.keys())
# The .keys() fucntion allows us to see all our keys
print(game_info.values())
# The .values() fucntion allows us to see all our values

username = "AbdullahAmod"
password = "Choclatecake11"
attempts = 3

while attempts > 0:
  user_input1 = input("Enter your username:")
  user_input2 = input("Enter your password:")
  if user_input1 == username:
    if user_input2 == password:
      "Correct login"
  else:
    attempts - 1
    if attempts == 0:
      "You have run out of attempts and are now locked out"
    else:
      "Incorrect login"
      "You have", attempts, " remaining"