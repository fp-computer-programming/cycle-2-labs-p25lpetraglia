#lab 8-4
# Lab 4: lab_8-4.py

def multiple_stuff(numbers):
   
    
    result = [num * i for i, num in enumerate(numbers)]
    return result


test_list1 = [10, 20, 30, 40]
test_list2 = [1, 2, 3, 4]

print("Test case 1:", multiple_stuff(test_list1)) 
print("Test case 2:", multiple_stuff(test_list2))