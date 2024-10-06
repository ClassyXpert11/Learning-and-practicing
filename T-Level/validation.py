def is_valid(name, age, course):
  valid = False

  if name.isdigit() == True:
    print("\nPlease enter only characters for your name")
    valid == False
  else:
    valid = True

  if age.isdigit() == False:
    print("\nPlease enter only numbers for your age")
    valid == False
  else:
    valid == True

  if course.isalpha() == False:
    print("\nPlease enter only characters for your course")
    valid == False
  else:
    valid == True
  return valid

name = input("Please enter your name: ")
age = input("Please enter your age: ")
course = input("Please enter your course: ")


valid = is_valid(name, age, course)

if(valid == True):
  print(f"Hello {name} + you are {age} years old." + f" You are currently on {course}, welcome to the course.")