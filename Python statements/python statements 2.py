#This code prints out even numbers from the range of 0 to 11
#It is 0 to 11 because if it was 1 to 10 python would not print the 0 and the 10 which are even numbers
# "a" is the variable here
#The for loop is checking through the range 
#The if statement comes after the for loop is done checking the the range

even_list = [a for a in range (0 ,11) if a%2 == 0]
print(even_list)

