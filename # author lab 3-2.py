# author lab 3-2
import random
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)
random.seed(42)  # Set the seed to a specific value
even_random_number = random.randrange(0, 101, 2)  # Generates an even number
print("Even number between 0 and 100:", even_random_number)
