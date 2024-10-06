def close(num1): #close is the name of the function and num1 is the name of the variable
  if num1 in range(85,120): #if the variable is in the range of these numbers then it will return true
    return True
  elif num1 in range(185,220): #if the variable is in the range of these numbers too then it will also return true
    return True
  else: #Otherwise it will return false
    return False

print(close(87))
print(close(189))
print(close(70))
print(close(170))

