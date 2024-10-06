#Activity
course_modules = ["Python Essentials", "Workshop", "Enterprise", "Networking", "Unity", "MOS"]

for x in course_modules:
#Any variable can be placed here
  if x == "Python Essentials":
    print(x)
    #The print needs to indented into the if statement always
  break
  #The break is preventing the print code to print that message multiple times (as many times as there are things in the list)



##Practice
fruits = ["Apple", "Banana", "Orange", "Peach"]

for a in fruits:
  if a == "Banana":
    print(a)

colours = ["Green", "Yellow", "Red", "Blue", "Purple"]

for b in colours:
  if b == "Blue":
    print(b + " is on the list")

randomstuff = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test10", "test11", "test12"]

for c in randomstuff:
  if c == "test1":
    print("Nice")
  if c == "test6":
    print("Also nice :)")
  


