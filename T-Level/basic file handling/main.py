my_file = open("files/myfile.txt")
my_file.seek(4)
print(my_file.readlines())
my_file.close()

with open("files/myfile.txt", "r+") as my_file:
   #do something here
  print(my_file.read())
  my_file.seek(0)
  print(my_file.readlines())

  my_file.write("This is my write text")
  my_file.write("\n\tthis is a sentence")
  print(my_file.read())



my_test = open("test.txt", "w")
# this is creating a file called "test.txt" and the "w" is writing 
my_test.write("Hello world")
# this is what we want to write
my_test.close()
# this is closing the file so the code above can actually work

with open("test.txt", "a") as my_test:
  # this is doing the same thing as above except we are using the "with" statement. we are also using the "a" mode to append something rather than write over it like "w" does. my_test is the variable here by the way.
  my_test.write("\nHello world")
  # this is what we want to write, and we don't need to close it because the "with" statement takes care of that
  