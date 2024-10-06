# The *args allows us to input multiple variables / arguments
def func_1 (*args):
  # This is returning 25% of what is printed below
  return sum((args))*0.25

# This equals 100 and 25% of 100 is 25
print(func_1(30,70))
# This equals 290 and 25% of 290 is 72.5
print(func_1(30,70,100,50,40))


# kwargs means Key Word Arguments
def func_2 (**kwargs):
  # If it finds the key word called "fruit" then it will print this
  if "fruit" in kwargs:
    print("Found some fruit")
    # If it finds the key word called "vegetable" then it will print this
  elif "vegetable" in kwargs:
    print("Found some vegetable instead")
    # Otherwise it will print this
  else:
    print("I did not find any fruit or vegetables")

# Here i am putting in the Key and Values of the kwargs 
func_2(fruit = "Apple", vegetable = "Peas")

#EXERCISE 1
def myfunc (*args):
  return sum(args)

print(myfunc(2,4,6,8,10,12))


#EXERCISE 2
def myfunc2 (num_list):
  even_list = []
  for number in num_list:
    if number %2==0:
      even_list.append(number)
    else:
      pass
  return even_list

print(myfunc2([1,2,3,4,5,6,7,8,9,10]))


#EXERCISE 3
def myfunc3(word):
  result = ""
  index = 0
  for letter in word:
    if index % 2 == 0:
      result += letter.lower()
    else:
      result += letter.upper()
    index += 1
  return result

print(myfunc3("qwertyuiop"))

