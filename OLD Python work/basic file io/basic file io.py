## This only reads it
with open("textFiles/myfile.txt", 'r') as f:
  print(f.read())
  #f.seek(4)
  #print(f.read(2))
  #print(f.readlines(1))

## This only writes (overwrites all content)
with open("textFiles/myfile.txt", 'w') as f:
  print(f.write("Hello World!"))

## This writes things at the end of content
with open("textFiles/myfile.txt", 'a') as f:
  print(f.write("Hello World!"))


#a = open("textFiles/myfile.txt")
#print(a.read(2))
#a.close()

b = open("test.txt", 'w')
b.write("Hello world")
b.close()

with open("test.txt", 'w') as c:
  print(c.write("Hello World!"))
  # Also works without print()

with open("test.txt", 'r') as c:
  print(c.read())

import os
os.remove("player.txt")

with open ("player.txt", 'a') as player:
  player.write("Player name: Jack\n")
  player.write("Health: 100\n")
  player.write("Mana: 1,000,000\n")
  player.write("List of weapons: Sword, Dagger, Spear, Bow, Arrows and Shield")
