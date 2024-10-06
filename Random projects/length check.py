while True:
  town = input("Enter a town name:\n")
  if len(town) > 15:
    print("\nName is too long, try again please")
    length = input("Enter a town name:\n")
  else:
    print("\nThat is a nice town!")
    break

