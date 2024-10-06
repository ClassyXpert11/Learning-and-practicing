my_list = ["Hello", 25, 5.90]
print(len(my_list))

my_list[1]

my_list = [1, 2, 3, 4, 5]
print(my_list[1:4:1])

random_list = ["Red", "Blue", "Green", "Orange", "Yellow", "Purple", "Pink", "Black"]
print(random_list[2:5:1])

name = "Abdullah Amod"


messages = ["welcome", "Abdullah Amod", "you are", "17", "years old"]
print("Unchanged: " + str(messages))
messages[1] = "Martin Rowe"
print("Changed: " + str(messages))

numbers = [33, 56, 5, 76, 23, 97]
print(numbers)
print(numbers)

popped_number = numbers.pop(1)
print(popped_number * 2)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

New_PC = ["Motherboard", "CPU", "GPU"]
other_parts = ["RAM", "SSD", "HDD", "Cooler"]
New_PC.append(other_parts)
print(New_PC)

nested = ["a", "b", "c", ["dd", "ee"], "f"]
print(nested[3][1])


#Task:
list_1 = ["Apple" , ["Red", "Green "], "Banana", "Orange"]
list_2 = ["Pear","Grapes",["Seeds", "Seedless"], "Tomatoes"]

#This is append list 2 at the end of list 1
list_1.append(list_2)
print(list_1)

#This is modify the item "Grapes" with "Plum"
list_2[1] = "Plum"
print(list_2)

#This is remove tomatoes from the list 2
print(list_2.pop(3))

#This is sort the list
#list_1.sort()
#list_2.sort()
#print(list_1 + list_2)

#This is apple and green from the list
print(list_1[0])
print(list_1[1][1])

#This is print "Green Apple" from the list
Green_Apple = (list_1[1][1]) + (list_1[0])
print(Green_Apple)

