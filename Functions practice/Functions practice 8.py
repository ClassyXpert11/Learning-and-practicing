def repeatedLetters(word): #repeatedLetters is the name of the function and word is the name of the variable
  tword = " " #creating a variable to use later
  for letter in word: #creating a for loop to go and check through the below code
    tword = tword + (letter*3) #getting the variable that was made earlier and multiplying the letters in that string by 3
  return tword

print(repeatedLetters("Hello"))
print(repeatedLetters("Mississippi"))

