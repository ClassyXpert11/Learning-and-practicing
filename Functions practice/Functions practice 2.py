def ac(text): #animal_crackers is name of the function and text is the name of the variable
  words = text.split() #this splits the words and places it in a variable
  return words[0][0] == words[1][0] #this compares first letter of first word with first letter of 2nd word and returns it either true or false
result = ac("Levelheaded Llama")
print(result)


def ac2 (text2):
  more_words = text2.split()
  return more_words[0][0] == more_words[1][0]

results2 = ac2("Crazy Kangaroo")
print(results2)


def ac3(text3):
  even_more_words = text3.split()
  return even_more_words[0][0] == even_more_words[1][0]

print(ac3("Hello, Hugo!"))


def ac4(text4):
  more_more_words = text4.split()
  return more_more_words [0][0] == more_more_words[1][0]

print(ac4("Marvelous Marty!"))

#def ac5(text5):
  
