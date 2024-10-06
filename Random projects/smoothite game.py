space = "##########################"

def pick_a_smoothie():
  print(f"{space}\nSmoothie flavours available:\n1) Strawberry\n2) Banana\n3) Pear\n4) Apple\n5) Pineapple")

  while True:
    smoothie_flavour = input("\nPlease pick a smoothie flavour (number): ")

    try:
      smoothie_flavour = int(smoothie_flavour)
      if smoothie_flavour == 1:
        print("you chose strawberry!")
      elif smoothie_flavour == 2:
        print("you chose Banana!")
      elif smoothie_flavour == 3:
        print("you chose Pear!")
      elif smoothie_flavour == 4:
        print("you chose Apple!")
      elif smoothie_flavour == 5:
        print("you chose Pineapple!")
      else:
        print(f"\n{space}\nPlease enter a number from 1 to 5\n{space}\n")
    except ValueError:
      print(f"\n{space}\nPlease enter a valid smoothie number\n{space}\n")


pick_a_smoothie()