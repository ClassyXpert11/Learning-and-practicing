a = 50
b = 51

if a > b:
  print("a is greater than b")
# If the first statement is true then it will print this
elif a < b:
  print("b is greater than a")
# If the second statement is true and the first statement is false then it will print this
else:
  print("a is equal to b")
#If both statements are false then it will print this


c = 1
d = 2
e = 3
f = 4

if f > c and e > d:
#The and in this statement tests out both conditions at the same time to see whether they are true or false
  print("Both f and d are greater than c and d")
else:
  print("Both f and d are not greater than c and d")


g = 5 
h = 6
i = 7
j = 8

if j > g or i < h:
#The or in this statements also tests both of them out but gives you the result of only one of the statements
  print("One of these statements is true")
