age = input("Please enter your age:\n")

while not age.isdigit():
  print("\nPlease enter numbers only!")
  age = input("Please enter your age:\n")

age = int(age)

if age < 18:
  print("\nYou are not old enough")
elif age == 18:
  print("\nYou are 18 years old!")
else:
  print("\nYou are over 18!")

