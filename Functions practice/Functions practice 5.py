def rev(abc): #Rev is the name of the function and abc is the name of the variable
  asf = abc.split(" ") #This just splits the code so that it can used it later
  return " ".join(reversed(asf)) #This joins the words together then reverses them using the split variable that was made earlier

print(rev("I am home"))
print(rev("We are ready"))

