#lab 8-1
total = 0

while True:
    try:
        number = int(input("Enter a number (-1 to quit): "))
        if number == -1:
            break  
        total += number  
    except ValueError:
        print("Please enter a valid number.")

print(f"The sum of all numbers entered is: {total}")