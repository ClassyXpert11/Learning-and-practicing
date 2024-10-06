def capital(macdonald): #captial is the name of the function and macdonald is the variable
  if len(macdonald) > 3: #if the length of the variable is is greater than 3 then is capitalizes it
    return macdonald[:3].capitalize() + macdonald[3:].capitalize() #this slices the some of the varible and then capitalizes them then adds them back together

print(capital("macdonald"))


