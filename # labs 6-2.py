# labs 6-2
#lp
def sum_of_evens():
   
    num = int(input("Enter a number: "))
    
   
    total = 0
    current = 2  

    
    while current <= num:
        total += current
        current += 2  

    print("The sum of even numbers from 1 to", num, "is:", total)


sum_of_evens()
