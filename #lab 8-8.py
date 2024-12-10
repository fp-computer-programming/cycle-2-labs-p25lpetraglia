#lab 8-8

for number in range(1, 101):
    if number % 2 == 0:
        even_sum += number
print(f"Sum of all even numbers between 1 and 100: {even_sum}")


secret_number = 7 
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            print("Number is out of range. Try again.")
        elif guess == secret_number:
            print("Congratulations! You guessed correctly.")
            break
        else:
            print("Incorrect, try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


for i in range(1, 6):
    print(str(i) * i)


words = ["python", "loops", "programming", "fun", "learn"]
for index, word in enumerate(words, start=1):
    print(f"{index}: {word}")


for number in range(1, 51):
    if number > 40:
        break
    if number % 3 == 0 and number % 5 == 0:
        continue
    print(number)


collected_integers = []
while len(collected_integers) < 5:
    try:
        user_input = int(input("Enter an integer: "))
        collected_integers.append(user_input)
    except ValueError:
        print("That's not an integer. Please try again.")
print(f"Collected integers: {collected_integers}")


original_string = "hello world"
reversed_string = ""
for char in original_string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")


while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            print("Please enter a positive integer.")
            continue
        digit_sum = 0
        for digit in str(number):
            digit_sum += int(digit)
        print(f"Sum of digits: {digit_sum}")
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
