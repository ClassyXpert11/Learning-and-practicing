import random

def validate_input(input_str):
    while True:
        user_input = input(input_str)
        if user_input.isnumeric():
            return int(user_input)
        else:
            print("Please enter numbers only.")

def update_high_scores(high_scores, name, guesses):
    if name in high_scores:
        if guesses < high_scores[name]:
            high_scores[name] = guesses
    else:
        high_scores[name] = guesses

def print_leaderboard(high_scores):
    sorted_scores = sorted(high_scores.items(), key=lambda x: x[1])
    print("\n--- Leaderboard ---")
    rank = 1
    for score in sorted_scores:
        print(f"{rank}. {score[0]} - {score[1]} guesses")
        rank += 1

def play_game():
    print("\nNew Game\n")
    random_number = random.randint(1, 100)
    num_of_guesses = 0
    while True:
        guess = validate_input("Guess a number between 1 and 100: ")
        num_of_guesses += 1
        if guess == random_number:
            print(f"\nCongratulations! You guessed the number in {num_of_guesses} tries.")
            return num_of_guesses
        elif guess > random_number:
            if guess - random_number >= 5:
                print("Too high! You are not even close.")
            elif guess - random_number == 4 or guess - random_number == 3 or guess - random_number == 2:
                print("Too high! You are nearly there.")
            else:
                print("Too high! You are incredibly close.")
        else:
            if random_number - guess >= 5:
                print("Too low! You are not even close.")
            elif random_number - guess == 4 or random_number - guess == 3 or random_number - guess == 2:
                print("Too low! You are nearly there.")
            else:
                print("Too low! You are incredibly close.")

def main():
    high_scores = {}
    while True:
        print("\n--- MENU ---")
        print("1. Play Game")
        print("2. View High Scores")
        print("3. Instructions")
        print("4. Quit")
        choice = validate_input("Enter your choice: ")
        if choice == 1:
            name = input("Enter your name: ")
            guesses = play_game()
            update_high_scores(high_scores, name, guesses)
        elif choice == 2:
            if not high_scores:
                print("\nThere are no high scores to display.")
            else:
                print_leaderboard(high_scores)
        elif choice == 3:
            print("\n--- INSTRUCTIONS ---")
            print("1. You will be given a range of numbers to guess from.")
            print("2. You will be prompted to enter a number.")
            print("3. You will be told if your guess is too high or too low.")
            print("4. Keep guessing until you guess the number.")
            print("5. Your score will be based on how many guesses you took.")
        elif choice == 4:
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
  main()