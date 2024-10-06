import random

leaderboard_file = "leaderboard.txt"

def update_leaderboard(player_name, difficulty, word_letters_left):
    """
    Update the leaderboard with the player's name, difficulty, and number of letters left.

    Args:
        player_name (str): The name of the player.
        difficulty (str): The difficulty level of the game.
        word_letters_left (int): The number of letters left in the word when the game ended.
    """

    # Check if leaderboard file exists, create if it doesn't
    try:
        with open(leaderboard_file, "r") as f:
            leaderboard = [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        with open(leaderboard_file, "w") as f:
            f.write("Player,Difficulty,Letters Left\n")
        leaderboard = []

    # Check if player already exists in the leaderboard, update score if they do
    for i, player_data in enumerate(leaderboard):
        if player_data[0] == player_name and player_data[1] == difficulty:
            if int(player_data[2]) >= word_letters_left:
                leaderboard[i][2] = str(word_letters_left)
            break
    else:
        leaderboard.append([player_name, difficulty, str(word_letters_left)])

    # Sort leaderboard in ascending order by number of letters left
    leaderboard.sort(key=lambda x: int(x[2]))

    # Write leaderboard to file
    with open(leaderboard_file, "w") as f:
        f.write("Player,Difficulty,Letters Left\n")
        for player_data in leaderboard:
            f.write(",".join(player_data) + "\n")

def hangman_game():
    """
    Play a game of hangman.
    """
    print("\nWelcome to Hangman! Let's get started!")
    player_name = input("Please enter your name:\n")

    # Check if player entered a name
    while not player_name:
        player_name = input("Please enter your name:\n")

    print(f"\nHello, {player_name}!\n")

  # Define the difficulties and their corresponding word lists
    difficulties = [
      ("Easy", ["cat", "dog", "fish", "tree", "apple"]),
      ("Medium", ["circle", "bicycle", "grape", "elephant", "dolphin"]),
      ("Hard", ["extravagant", "resilience", "authenticity", "perseverance", "imagination"]),
      ("NIGHTMARE", ["accomplishment ", "electrocardiogram", "extracurricular", "internationalization ", "multifunctionality"])
    ]

    # Sort difficulties by maximum word length
    difficulties.sort(key=lambda x: len(max(x[1], key=len)))

    # Print the difficulties to the user
    print("Please select a difficulty level:\n")
    for i, (difficulty, word_list) in enumerate(difficulties):
      print(f"{i+1}. {difficulty} ({len(min(word_list, key=len))}-{len(max(word_list, key=len))} letters)")

    # Ask the user to select a difficulty level
    while True:
      try:
        difficulty_choice = int(input("\nEnter the number of the difficulty you would like to play: "))
        if difficulty_choice not in range(1, len(difficulties)+1):
            raise ValueError
        break
      except ValueError:
        print(f"Invalid input. Please enter a number between 1 and {len(difficulties)}.")

  # Set the difficulty and randomly select a word from the corresponding word list
    difficulty, word_list =     difficulties[difficulty_choice-1]
    word = random.choice(word_list)
    print(f"\nYour word has {len(word)} letters.\n")

    # Create a list of underscores to represent the letters of the word
    word_letters = list(word)
    word_letters_left = len(word_letters)
    for i in range(len(word_letters)):
      if word_letters[i] in string.ascii_letters:
        word_letters[i] = "_"
        word_letters_left -= 1
    word_letters_left = str(word_letters_left)


  # Play the game
    incorrect_guesses = 0
    guesses = []
    while incorrect_guesses < 6 and word_letters_left != "0":
      print(f"{' '.join(word_letters)}\n")
      print(f"Incorrect guesses: {', '.join(guesses)}\n")
      guess = input("Guess a letter: ").lower()
      while guess in guesses:
        guess = input("You've already guessed that letter. Guess a different letter: ").lower()
      guesses.append(guess)
      if guess in word:
        for i in range(len(word)):
          if word[i] == guess:
                word_letters[i] = guess
                word_letters_left = str(int(word_letters_left)-1)
        print("Correct!\n")
    else:
        incorrect_guesses += 1
        print("Incorrect!\n")
        if incorrect_guesses == 6:
            print("Game over! You've run out of guesses.")
            print(f"The word was {word}. Better luck next time, {player_name}!")
        else:
            print(f"You have {6-incorrect_guesses} guesses left.\n")

  # Update the leaderboard
    update_leaderboard(player_name, difficulty, int(word_letters_left))

    # Ask the user if they want to play again
    play_again = input("Would you like to play again? (y/n)").lower()
    while play_again not in ["y", "n"]:
      play_again = input("Invalid input. Please enter 'y' or 'n': ").lower()
    if play_again == "y":
      hangman_game()
    else:
      print("Thanks for playing! Goodbye.") 

def display_instructions():
    print("\nWelcome to Hangman!")
    print("The goal of the game is to guess the secret word before you run out of attempts.")
    print("Here's how to play:")
    print("1. The computer will choose a random word and display the number of letters in the word.")
    print("2. You will guess one letter at a time.")
    print("3. If your guess is correct, the letter will be revealed in the word.")
    print("4. If your guess is incorrect, you will lose an attempt.")
    print("5. You have a total of 6 attempts to guess the word.")
    print("6. If you guess the word correctly within 6 attempts, you win!")
    print("7. If you run out of attempts before guessing the word, you lose.")


def show_leaderboard():
  with open(leaderboard_file, "r") as file:
    file_contents = file.read()
  print(file_contents)


def main_menu():
    while True:
        print("\nMAIN MENU:")
        print("1. Play Game")
        print("2. Leaderboard")
        print("3. How to Play")
        print("4. Quit Game")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            hangman_game()
        elif choice == "2":
            show_leaderboard()
            input("\nPress Enter to continue...")
        elif choice == "3":
            display_instructions()
            input("\nPress Enter to continue...")
        elif choice == "4":
            print("\nThanks for playing Hangman!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()




