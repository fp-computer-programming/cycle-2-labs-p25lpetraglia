#8-6
# Lab 6: add_foods
def add_foods(food_list):
    sixth_letter = []
    not_foods = []
    short_foods = []
    
    for food in food_list:
        try:
            sixth_letter.append(food[5]) 
        except TypeError:  
            not_foods.append(food)
        except IndexError:  
            short_foods.append(food)
    
    print("sixth_letter:", sixth_letter)
    print("not_foods:", not_foods)
    print("short_foods:", short_foods)


add_foods(["banana", "grapefruit", 123, "kiwi", "orange"])
