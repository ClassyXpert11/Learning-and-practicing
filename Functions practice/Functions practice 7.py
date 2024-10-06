def threes(num1): #threes is the name of the function and num1 is the variable
  if num1[0] == num1[1] == 3 or num1[1] == num1[2] == 3: #if the first and second number are 3 or the second and third number are 3 then it will return true
    return True
  else: #Otherwise it will return false
    return False

print(threes([3,3,1]))
print(threes([1,3,3]))
print(threes([1,3,1,3]))
print(threes([3,1,3]))

