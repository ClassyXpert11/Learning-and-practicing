person_1 = {"name" : "Abdullah", "age" : 18, "height" : 3.5}
print(person_1)

person_1 ["hobbies"] = ["Gaming", "Coding", "Watching movies"]
# instead of using .append to add things to the dictionary we just used the [] and then add the stuff after
print(person_1["hobbies"][1])
# this is taking out the one thing from the list (value rather than the whole key)

person_1 ["name"] = "Tim"
# this replaces the name in the already made dictionary
print(person_1)

students = {"student1" : {"name" : "Hope", "age" : 16, "height" : 2.5}, "student2" : {"name" : "Jack", "age" : 17, "height" : 2.7}}
# this is a nested dictionary. we created a key first then made another dictionary for that specific key. you can have multiple of these
print(students["student1"]["name"])
# printing this is slightly different because we want student one's name specifically, so after putting the variable we put the key then the value in square brackets

#-------------------------------------PRACTICE--------------------------------------------------
animals = {"dog" : {"age" : 1, "name" : "Peter", "months it was owned" : 14}, "cat" : {"age" : 3, "name" : "Brian", "months it was owned" : 18}, "parrot" : {"age" : 2, "name" : "Jason", "months it was owned" : 8}}
print(animals["parrot"]["name"])

animals["dog"]["name"] = "Bruce"
print(animals["dog"]["name"])


d = {"names" : ["Jai", "Paramjit", "Tim"], "age" : [27, 37, 47] }
print(d["names"][1])