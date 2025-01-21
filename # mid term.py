# Midterm Project
# Nate Estrella + Logan Petraglia


#wordle project 


import random

def choose_target_word(difficulty):
    """Choose a random word from a predefined list based on difficulty."""
    easy_words = ["apple", "grape", "melon", "pearl", "chair"]
    medium_words = ["bacon", "flute", "brand", "stone", "plant"]
    hard_words = ["quilt", "vivid", "prism", "crypt", "glyph"]
    


    if difficulty == "easy":
        return random.choice(easy_words)
    elif difficulty == "medium":
        return random.choice(medium_words)
    elif difficulty == "hard":
        return random.choice(hard_words)
    else:
        print("Invalid difficulty. Defaulting to easy.")
        return random.choice(easy_words)



def check_guess(target_word, guess):
    """Check the guess and provide feedback."""
    feedback = []
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            feedback.append(f"Yes, the letter '{guess[i]}' is correct and in the right spot!")
        elif guess[i] in target_word:
            feedback.append(f"Yes, the letter '{guess[i]}' is correct but not in the right spot.")
        else:
            feedback.append(f"The letter '{guess[i]}' is not in the target word.")
    return feedback



def display_hint(target_word, guessed_letters):
    """Provide a hint by revealing a random letter from the target word."""
    available_hints = [letter for letter in target_word if letter not in guessed_letters]
    if available_hints:
        hint_letter = random.choice(available_hints)
        print(f"💡 Hint: The word contains the letter '{hint_letter}'.")
    else:
        print("No more hints available!")



def play_again():
    """Ask the player if they want to play again."""
    while True:
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")



def select_difficulty():
    """Ask the player to select a difficulty level."""
    while True:
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Invalid choice. Please type 'easy', 'medium', or 'hard'.")



def play_game():
    """Main game function."""
    points = 0
    guessed_letters = []

    print("Welcome to Wordle!")
    difficulty = select_difficulty()

    while True:
        target_word = choose_target_word(difficulty)
        attempts = 5

        print(f"Try to guess the {len(target_word)}-letter target word!")

        for attempt in range(attempts):
            guess = input(f"Attempt {attempt + 1}/{attempts}: Enter a {len(target_word)}-letter word: ").lower()

           
            if len(guess) != len(target_word):
                print(f"Your word must be exactly {len(target_word)} letters. Try again.")
                continue

            
            guessed_letters.extend([letter for letter in guess if letter not in guessed_letters])

            
            if guess == target_word:
                points += 1
                print(f"🎉 Congratulations! You guessed the word: {target_word}")
                print(f"Good job! You now have {points} point{'s' if points > 1 else ''}.")
                break

            
            feedback = check_guess(target_word, guess)
            for message in feedback:
                print(message)

           
            if attempt == 2:
                display_hint(target_word, guessed_letters)
        else:
            print(f"Sorry, you've used all attempts. The correct word was: {target_word}.")

      
        if not play_again():
            print(f"Thanks for playing! Your final score is {points} point{'s' if points > 1 else ''}. Goodbye!")
            break

        

if __name__ == "__main__":
    play_game()


