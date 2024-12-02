#lab 8-2

numbers = [2, 3, 5, 6, 9, 10, 12, 14, 15]

print("Multiples of 3 in the list:")
for number in numbers:
    if number % 3 != 0:
        continue  
    print(number)
