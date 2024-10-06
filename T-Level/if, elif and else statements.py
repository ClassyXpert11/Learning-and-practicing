grade = int(input("Please enter your grade mark\n"))
# usually python doesn't take strings as integers so you'll have to put int() before the input() so that it can actually understand that you want it to be an integer rather than a string.

if grade >= 80:
  print("Distinction")
  # have to do highest number first so that it doesn' stop right away
elif grade >= 60:
  print("Merit")
elif grade >= 40:
  print("Pass")
else:
  print("Fail")
