my_name = "Abdullah Amod"
my_age = 18
print("Hello world. My name is {}, my age is {}".format(my_name, my_age))

dessert = "Ice cream"
snack = "Choclate"
print("My favourite snack is {1} and my favourite dessert is {0}!".format(dessert, snack))
# using index here so 1 would be snack and zero would be dessert. You can also use a = snack and b = dessert.

print(f"My name is {my_name}, my age is {my_age}")
# this is another way to use the .format(). This one just looks neater although they do the same thing

result = 100/777
print("The result was {r:1.2f}".format(r = result))
# this rounds the number up to 2 decimal places. You can change to 1.3 or 1.4 as well.