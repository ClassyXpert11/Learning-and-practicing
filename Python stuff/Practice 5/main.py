import random

person = int(input("Enter a number from 1 or 2: "))
cpu = random.randint(1, 2)
wanna_continue = input("Would you like to play again?")

while person == cpu:
    print(person)
    print(cpu)
    if person == cpu:
        print("We got the same number bro")
    print(wanna_continue)
    if wanna_continue == "yes":
        print("REPEATING")
        continue
    elif wanna_continue == "no":
        print("STOPPING")
    break
    if person != cpu:
        print("Different number moment")
        print(wanna_continue)
    if wanna_continue == "yes":
        print("REPEATING")
        print(person)
        print(cpu)
    elif wanna_continue == "no":
        break