list_1 = [1, "hello", True, [1,2,3,4,[5,6,7,8]]] 
print(list_1[3][4][2])
# its taking 7 from this nested list

fruits = ["Apple", "Orange", "Banana"]
print(fruits)

fruits.append("Strawberry")
print(fruits)
# adding this string at the end of the list

frt = fruits.pop(3)
# deleting a word from the list and storing it in a variable
print(fruits)
print(frt)

a = "Hello world!"
print(list(a))
# using split() to separate each word and letter

print(len(a))
print(len(fruits))
# finding out the length of each list

print(fruits[1::])
# slicing so everything after the first word will come

fruits.sort()
print(fruits)
# it got sorted alphabetically. If there were numbers in the list then they would get sorted lowest to highest

fruits.reverse()
print(fruits)
# it printed things in reverse order (in the latest version of the list)

pc_list = ["Motherboard", "CPU", "GPU"]
pc_list.append("RAM")
pc_list.append("SSD")
pc_list.append("HDD")
pc_list.append("Cooler")
print(pc_list)


#------------------------------------ ACTIVITY -----------------------------------------------

list_a = ["Apple", ["Red", "Green"], "Banana", "Orange"]
list_b = ["Pear", "Grapes", ["Seed", "Seedless"], "Tomatoes"]

list_a.append(list_b)


list_b[1] = "Plum"


list_b.pop(3)


# cannot sort a nested array

print(list_a[0], list_a[1][1])

green_apple = list_a[1][1], list_a[0]
print(green_apple)