dict_1 = {"Name" : "Jai Somaiya", "Age" : 26, "Hobbies" : ["Eating", "Sleeping", "Coding"]}

dict_1["Height"] = 5.9

print(dict_1)

var_1 = {"fruit1" : "apple", "Colours" : {"colour1" : "Red", "colour2" : "Green" } }
print(var_1)

print(var_1.keys())
print(var_1.values())
print(var_1.items())


#Activity

#Name, age, course and list of 3 hobbies
dict_2 = {"Name" : "Abdullah Amod", "Age" : "17", "Course" : "C7322", "Hobby1" : "Watching movies or shows", "Hobby2" : "Going outside", "Hobby3" : "sleeping"}

#Display the dictionary
print(dict_2)

#Display the keys
print(dict_2.keys())

#Display the values
print(dict_2.values())

#Display one hobby
one_hobby = dict_2["Hobby3"]
print(one_hobby)



#Practicing dictionaries 


#This is a dictionary for cars
Practice_dict = {"Car companies" : "Audi " "BMW " "Tesla " "KIA", "Additional car comapnies" : {"Honda " "Ford " "Toyota " "Mercedes "}, "Car types" : "Petrol " "Diesel " "Electric"}

print(Practice_dict.keys())
print(Practice_dict.values())

# This shows all the car companies names together rather than a seperate list
all_car_compaines = Practice_dict["Car companies"], Practice_dict["Additional car comapnies"]
print(all_car_compaines)

car_types = Practice_dict["Car types"]
print(car_types)


#This is a dictionary for some smoothie recipes
smoothie_recipes_dict = {"Strawberry smoothie recipe" : "5 - 7 hulled strawberries, " "2 tea spoons of sugar, " "Milk" , "Banana smoothie recipe" : "1 large banana or 2 small bananas, " "2 tea spoons of sugar, " "Milk", "Strawberry and banana smoothie recipe" : "6 hulled strawberries, " "1 banana, " "2 tea spoons of sugar, " "Milk"}

print(smoothie_recipes_dict.keys())
print(smoothie_recipes_dict.values())

Strawberry_and_banana_smoothie_recipe = smoothie_recipes_dict["Strawberry and banana smoothie recipe"]
print(Strawberry_and_banana_smoothie_recipe)


#This is a dictionary for some flowers and the colours they come in
flowers_dict = {"Common types of flowers" : "Rose, " "Tulips, " "Carnation", "Different colours of roses" : {"Red, " "White, " "Yellow"}, "Different colours of tulips" : {"Orange, " "White, " "Purple"}, "Different colours of carnations" : {"Pink, " "Yellow, " "Red"}, "Rare types of flowers" : "Orchids, " "Jade vines, " "Corpse flower", "Different colours of Orchids" : {"Blue, " "Red, " "Green"}, "Different colours of Jade vines" : "Brown, " "Green, " "Purple", "Different colours of Corpse flowers" : "Purple, " "Green, " "Red"} 

print(flowers_dict.keys())
print(flowers_dict.values())

Flower_names = flowers_dict["Common types of flowers"], flowers_dict["Rare types of flowers"]
print(Flower_names)

Flower_colours = flowers_dict["Different colours of roses"], flowers_dict["Different colours of tulips"], flowers_dict["Different colours of carnations"], flowers_dict["Different colours of Orchids"], flowers_dict["Different colours of Jade vines"], flowers_dict["Different colours of Corpse flowers"]
print(Flower_colours)