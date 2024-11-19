#Lab 7-5 lp


def sum_even_numbers():
   
    numbers = []
    print("Please enter 7 numbers:")
    for i in range(7):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    

    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    
    print(f"The total sum of even numbers given was {even_sum}")


if __name__ == "__main__":
    sum_even_numbers()
