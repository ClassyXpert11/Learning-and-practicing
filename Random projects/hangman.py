import random

def draw_hangman(lives):
    if lives == 6:
        print("  ________")
        print("  |      |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|")
    elif lives == 5:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|")
    elif lives == 4:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print("  |      |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|")
    elif lives == 3:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print(" /|      |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|")
    elif lives == 2:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print(" /|\     |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|")
    elif lives == 1:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print(" /|\     |")
        print(" /       |")
        print("         |")
        print("         |")
        print("_________|")
    elif lives == 0:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print(" /|\     |")
        print(" / \     |")
        print("         |")
        print("         |")
        print("_________|")


words = ["python", "programming", "hangman", "game", "computer"]
word = random.choice(words).lower()
guessed_letters = set()
lives = 6


while lives > 0:
    word_list = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(word_list))
    if set(word_list) == set(word):
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
    elif guess in word:
        guessed_letters.add(guess)
        print("Good guess!")
    else:
        guessed_letters.add(guess)
        lives -= 1
        print("Bad guess!")
        draw_hangman(lives)

if lives == 0:
    print(f"You lost! The word was {word}.")

