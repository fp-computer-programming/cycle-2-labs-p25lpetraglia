# Cura Personalis Mad Lib Game
# Authors: Logan Petraglia and Nate Estrella
# Date: 10/21/2024

import time

def print_intro():
    """Print the introduction to the Mad Lib game."""
    print("Welcome to the Cura Personalis Mad Lib!")
    print("Fill in the blanks to complete a story about Cura Personalis.")
    print("Cura Personalis is a Jesuit value that emphasizes the care for the whole person.")
    print("Let's explore how you would show care through this fun activity.\n")
    time.sleep(1)

def play_again():
    """Ask the player if they want to play again."""
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == 'yes':
            print("Great! Let's play again!\n")
            return True
        elif choice == 'no':
            print("Thank you for playing! See you next time!\n")
            return False
        else:
            print("Please answer with 'yes' or 'no'.\n")

def get_valid_input(prompt):
    """
    Prompt the user for input and validate it to ensure it consists
    only of alphabetic characters. Optional entries are also allowed.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.isalpha() or user_input == "":
            print(f"Accepted: {user_input}\n")
            return user_input
        else:
            print("Invalid entry. Please use only alphabetical characters.\n")

def get_inputs():
    """Gather all necessary inputs for the Mad Lib story."""
    print("\nLet's get started! Please provide the following words:\n")
    
    
    adj1 = get_valid_input("Enter an adjective: ")
    noun1 = get_valid_input("Enter a noun: ")
    verb1 = get_valid_input("Enter a verb (action word): ")
    adj2 = get_valid_input("Enter another adjective: ")
    noun2 = get_valid_input("Enter another noun: ")
    verb2 = get_valid_input("Enter another verb: ")
    adj3 = get_valid_input("Enter another adjective: ")
    noun3 = get_valid_input("Enter another noun: ")
    place1 = get_valid_input("Enter a place: ")
    emotion1 = get_valid_input("Enter an emotion: ")
    action1 = get_valid_input("Enter an action: ")
    adj4 = get_valid_input("Enter another adjective: ")
    noun4 = get_valid_input("Enter another noun: ")
    plural_noun1 = get_valid_input("Enter a plural noun: ")
    adj5 = get_valid_input("Enter another adjective: ")
    noun5 = get_valid_input("Enter another noun: ")
    emotion2 = get_valid_input("Enter another emotion: ")
    action2 = get_valid_input("Enter another action: ")
    
 
    adj6 = get_valid_input("Enter a final adjective (optional): ")
    noun6 = get_valid_input("Enter a final noun (optional): ")
    
    
    return (adj1, noun1, verb1, adj2, noun2, verb2, adj3, noun3, place1,
            emotion1, action1, adj4, noun4, plural_noun1, adj5, noun5,
            emotion2, action2, adj6, noun6)

def display_story(inputs):
    """Use inputs to create and display the Mad Lib story."""
    
    (adj1, noun1, verb1, adj2, noun2, verb2, adj3, noun3, place1, emotion1,
     action1, adj4, noun4, plural_noun1, adj5, noun5, emotion2, action2,
     adj6, noun6) = inputs
    
    print("\n--- Your Cura Personalis Mad Lib Story ---")
    
    
    story = (
        f"Cura Personalis is the {adj1} practice of caring for the {noun1} as a whole.\n"
        f"Every day, Jesuits {verb1} to show compassion and {adj2} care for those in need.\n"
        f"Whether it’s a {noun2} or {verb2} to help, the goal is always to be {adj3}.\n"
        f"One day, a Jesuit was walking {place1} and felt {emotion1}.\n"
        f"He decided to {action1} and help a {adj4} {noun4}.\n"
        f"The Jesuit was joined by other {plural_noun1}, all working together to make the world a more {adj5} place.\n"
        f"In the end, the {noun5} felt {emotion2}, and the Jesuits knew their {action2} made a difference.\n"
    )
    
    
    if adj6 or noun6:
        story += f"They even found a {adj6} {noun6} during their mission of care!\n"

    print(story)
    print("Thank you for playing the Cura Personalis Mad Lib!\n")
    time.sleep(1)

def game_summary():
    """Print a summary of the game and its purpose."""
    print("This Mad Lib game is inspired by the Jesuit principle of 'Cura Personalis',")
    print("which encourages us to take care of the whole person—body, mind, and spirit.")
    print("Remember that small actions, like those in the story, can make a big difference.")
    print("We hope this activity brought some fun into reflecting on this value!\n")
    time.sleep(1)

def main():
    """Main function to run the Cura Personalis Mad Lib Game."""
    print_intro()  
    
    
    while True:
        inputs = get_inputs()  
        display_story(inputs)  
        game_summary()        
        
        if not play_again():   
            break
    
    print("Thanks for playing! Have a great day!")
    time.sleep(1)


if __name__ == "__main__":
    main()

def unused_word_warning(adj6, noun6):
    """Warn the player if optional words are not used in the story."""
    if not adj6 and not noun6:
        print("Note: You skipped the optional words. They can add a twist to your story!\n")
    elif adj6 and not noun6:
        print(f"Great choice on using '{adj6}'! Adding it to the story made it more vivid!\n")
    elif noun6 and not adj6:
        print(f"The word '{noun6}' adds depth to the story. Nice choice!\n")
    else:
        print(f"Awesome! Both '{adj6}' and '{noun6}' added extra flair to your story.\n")
    time.sleep(1)

def validate_story_length(story):
    """Provide feedback on story length to enhance the game experience."""
    print("\n--- Story Feedback ---")
    if len(story) > 500:
        print("This is a lengthy story! Great job making it detailed!\n")
    elif len(story) > 300:
        print("Nice story length! It has a good balance of detail and brevity.\n")
    else:
        print("A shorter story can be powerful! You went straight to the heart of Cura Personalis.\n")
    time.sleep(1)


def display_story(inputs):
    
    (adj1, noun1, verb1, adj2, noun2, verb2, adj3, noun3, place1, emotion1,
     action1, adj4, noun4, plural_noun1, adj5, noun5, emotion2, action2,
     adj6, noun6) = inputs
    
    print("\n--- Your Cura Personalis Mad Lib Story ---")

    
    story = ()
    f"Cura Personalis is the {adj1} practice of caring for the {noun1} as a whole.\n"
    f"Every day, Jesuits {verb1} to show compassion and {adj2} care for those in need.\n"
    
    unused_word_warning(adj6, noun6)  

    
    validate_story_length(story)  
