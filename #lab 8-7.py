#lab 8-7

def add_nums(number_list):
    try:
        user_input = int(input("Enter a number: "))
        new_list = [num + user_input for num in number_list]
        print("Resulting list:", new_list)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    finally:
        print(f"Passed list: {number_list}; User input: {'Invalid' if 'user_input' not in locals() else user_input}")
add_nums([1, 2, 3]) 
add_nums([1, 2, 3])  
add_nums([-1, 0, 1])  
