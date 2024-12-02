#8-3


def process_numbers(numbers):
    """
    Processes a list of numbers.
    The function stops processing if it encounters a negative value (break),
    or skips even numbers (continue) and prints only odd ones.
    """
    print("Processing numbers:")
    for num in numbers:
        if num < 0:
            print("Negative value encountered. Stopping processing.")
            break 
        if num % 2 == 0:
            continue 
        print(num) 


numbers = [1, 4, 7, -2, 9, 12]
process_numbers(numbers)
