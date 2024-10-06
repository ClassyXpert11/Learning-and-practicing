dick = {"Sentinel lands": "Exultia, " "Taras Nabad, " "Sentinel Prime",
        "Hell locations": "Nekravol, " "Kagdinir Sanctum, " "Immora"}
print(dick.keys())
print(dick.values())

a = "I wish Hugo "
b = "Martin was my dad "
c = "I wish Hugo Martin was my dad!"
print(a + b + c)

game_name = "Marvel's Spider-man"
rating = "9/10"
recommend = "I would absolutely recommend it"
print(game_name + " is a very good game like seriously it's a " + rating + " and " + recommend)

hero = "Spider-Man"
print(hero.replace("Spider", "Ant").upper())

num1 = 11
print(str(num1) + " is my lucky number")
# The str() allows us to use that plus symbol and the string to make a sentence together.
# If that was not there then it would print an error

name = input("What is your name?\n")
print("Your name is " + name + "? I like that name!")
age = input("How old are you tho?")
#print(age + "? Cool!")
if 19 > age:
        print("Wow that's pretty young")
elif age > 20:
        print("You're in your twenties, cool!")
elif age > 30:
        print("You're in your thirties, cool!")
elif age > 40:
        print("You're in your fourties, cool!")
elif age > 50:
        print("Wow you're getting pretty old huh, no worries though! Life is still enjoyable bro!")

