i = 1
while i <= 12:
# the while loop will keep on repeating if the number is under or equal to 12
  if i == 1:
    num1 = int(input("Enter a number\n"))
    # this if statment is saying that it should only ask the user for their input if i equals one otherwise it will not ask
  print("{} x".format(i), num1," = {}".format(i*num1))
  # this is using formatting to basically say 1 x 2 = 2. So it puts i in those {} brackets then the user inputted number then whatever the answer is at the end. This is more of a visual thing to show the working out basically.
  i += 1
  # i = i + 1 is also the same thing. After the while loop is done it will add one to i and will keep doing so until it has reached 12
else:
  print("Done")
  # once i is equal to 12 it will print this to show it is complete