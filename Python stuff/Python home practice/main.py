# Basic calculator
#num1 = input("Enter number: \n")
#num2 = input("Enter another number: \n")
#result = float(num1) + float(num2)
#print(result)

# Mad libs game
#adjective = input("Enter an adjective: ")
#plural_noun = input("Enter a plural noun: ")
#person_name = input("Enter a person's name: ")
#print("\n")

#print("Pokemon are " + adjective)
#print(plural_noun + " are " + adjective)
#print(person_name + " is " + adjective)


# Lists

#list1 = ["Hell on Earth", "Exultia", "Cultist Base", "Doom Hunter Base",
         #"Super Gore Nest", "Arc Complex"]
#list1[1] = "Taras Nabad"
#print(list1[1])
#print(list1[2:6])


# trying out functions

def tsturo():
    print("DOOM Gaming")

tsturo()

#def potions(ptns):
    #return ptns+ptns+ptns
# after return is placed any line of code afterwards
# will not mean anything and will not run
#print(potions(10))
# making it print it 10 times
# so 3x10 basically

is_witcher = False
is_geralt = True

if is_witcher and is_geralt:
    print("Kill a monster for me?. Mutant...")
# This line will print if both variables are true
elif is_geralt:
    print("WITCH FUCKER!!!!!")
# This line will print if only is_geralt is true
elif is_witcher:
    print("Sir, the Leshen has attakced our village, please kill it...?")
# This line will print if only is_witcher is true
else:
    print("You're a regular guy then?")
# Otherwise if all are false then this will print out