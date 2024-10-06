def number(num1,num2): #number is the name of the function and num1 and num2 are the name of the variable
  if num1 == 20 or num2 == 20 or (num1+num2)== 20: #if num1 is 20 or num2 is 20 or both num1 and num2 are equal to 20 then it will return true 
    return True
  else: #otherwise it will return false
    return False

print(number(16,4))
print(number(20,1))
print(number(6,20))
print(number(6,4))


