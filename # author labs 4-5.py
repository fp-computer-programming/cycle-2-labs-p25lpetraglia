# author labs 4-5
# Create a Python file named lab_4-5.py


def count_letter():
   
    letter = input("Enter a letter: ").lower()  
    food_name = input("Enter a food name: ").lower()  

    count = 0
    
    for char in food_name:
        
        if char == letter:
            count += 1
    
    return count

print(f"The letter appears {count_letter()} time(s) in the food name.")
