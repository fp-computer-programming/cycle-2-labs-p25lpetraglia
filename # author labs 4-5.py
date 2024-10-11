# author labs 4-5



def count_letter():
   
    letter = input("Enter a letter: ").lower()  
    food_name = input("Enter a food name: ").lower()  

    count = 0
    
    for char in food_name:
        
        if char == letter:
            count += 1
    
    return count

print(f"The letter appears {count_letter()} time(s) in the food name.")
