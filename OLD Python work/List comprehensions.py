#This code is going to print the word "Hello" but separated
my_string = "Hello"

my_list = []
for letter in my_string:
  my_list.append(letter)

print(my_list)

#This code does the same thing as the above code does but in one line of code
my_list = [letter for letter in my_string]
print(my_list)
 
#This code is only printing multiples of 2 from a list
#If you change the number next to the % then it will print multiples of that number
#The range is just there to show you how far the multiples can go (from 0 to 11)
list_1 = [x for x in range (0 ,11) if x%2 == 0]
print(list_1)

#This code also does what the above code does but this time it says "Odd when the number is not a multiple of whatever is next to the %" 
list_2 = [x if x%2==0 else "Odd" for x in range (0, 11)]
print(list_2)

#This code is multiplying x and y together but in the list order they come in
#So 2 x 1 = 2 and 2 x 10 = 20 and 2 x 100 = 200 
#This applies to the rest of the numbers there
list_3 = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]
print(list_3)