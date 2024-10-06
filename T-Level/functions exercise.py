def lesser_even(num1, num2):
  # creating a function with the name lesser_even with variable inside the brackets
  if (num1 % 2 or num2 % 2) == 0:
    # checking if the variables are even with mod
    if num1 < num2:
      # checking which numbers are greater
      print(num1)
    elif num2 < num1:
      print(num2)
      # it should print out the greater number
  if (num1 % 2 or num2 % 2) != 0:
    # checking which number is not even
    if num1 > num2:
      print(num1)
    elif num2 > num1:
      print(num2)
      # printing the greater one

lesser_even(2,4)
lesser_even(2,5)


def animal_crackers(text):
  words = text.split()
  # splitting it up
  if words [0][0] == words [1][0]:
    # checking the first letter of the first word and first letter of the second word
    return True
    # returning true if they are the same
  else:
    return False
    # returning false if they are not the same
    
print(animal_crackers("Levelheaded Llama"))
#printing it so the outputs shows either true or false
print(animal_crackers("Crazy Kangaroo"))



def makes_twenty(num1, num2):
  if num1 == 20 or num2 == 20 or (num1 + num2) == 20:
    # checking if the num variables make 20 or have 20 in them
    return True
  else:
    return False

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))



def old_macdonald(name):
  return name[:3].capitalize() + name[3:].capitalize()
  # using slicing to select where we want to capitalise

print(old_macdonald("macdonald"))



def master_yoda(reverse_text):
  split_txt = reverse_text.split(" ")
  # splitting the text up and putting it into a variable
  print(" ".join(reversed(split_txt)))
  # joining them up together and reversing it. reversed() is just another way of using reverse(). the " " has to be in the split so that the join function knows what to join together

master_yoda("i am home")
master_yoda("we are ready")



def almost_there(num1):
  if num1 in range(90,111) or num1 in range(190, 211):
    # checking if num1 is in the range of either of these and if it is it will return true
    return True
  else:
    # otherwise false
    return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))



def has_33(num1):
  if num1[0] == num1[1] == 3 or num1[1] == num1[2] == 3:
    # checking if 3 is next to each other by using indexing
    return True
  else:
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))



def paper_doll(letter):
  ltrs = " "
  # making an empty variable for later use
  for multiple in letter:
    # putting it in a for loop so that we can actually get three letter each time
    ltrs = ltrs + (multiple*3)
    # multiplying the letter 3 times
  return ltrs

print(paper_doll("Hello"))
print(paper_doll("Mississippi"))



def summer_69(num1):
  bool = True
  # making a boolean to use later
  num2 = 0
  # making an empty integer
  for num3 in num1:
    # making a for loop to check through all the numbers
    if bool ==  False:
      if num3 == 9:
        bool = True
        # checking for a 9
    elif num3 == 6:
      bool = False
      # checking for a 6
    else:
      num2 += num3
      # adds them together 
  return num2

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))


def spy_game(num1):
  code = [0, 0, 7, 'x']
  # making a list to check the values that the user inputs
  for num2 in num1:
    # checking through it
    if num2 == code[0]:
      code.pop(0)
      # this removes 007 if it is there in that order
  return len(code) == 1

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))



def count_primes(num1):
  num2 = 0
  for num3 in range(num1):
    if num3 <= 1:
      continue
    for num4 in range(2, num3):
      if num3 % num4 == 0:
        break
    else:
      num2 += 1
  return num2

print(count_primes(100))
print(count_primes(200))
print(count_primes(300))


def print_big():
  letters = {
    "a" : "  *  \n *  *\n ****\n *  *\n *  *",
    "b" : "*\n*\n***\n*  *\n***",
    "c" : "  ****\n *\n*\n*\n*\n *\n  ****",
    "d" : "  *\n  *\n***\n* *\n***",
    "e" : " **\n*  *\n****\n*\n*\n **"
  }
  # these are where the letters are stored
  pick = input("Pick a letter between a - e\n")
  # asking the user
  if pick == "a":
    # if they picked a it will print that out but bigger from the dictionary i made
    print(letters["a"])
  elif pick == "b":
    print(letters["b"])
  elif pick == "c":
    print(letters["c"])
  elif pick == "d":
    print(letters["d"])
  elif pick == "e":
    print(letters["e"])

print(print_big())
     

  