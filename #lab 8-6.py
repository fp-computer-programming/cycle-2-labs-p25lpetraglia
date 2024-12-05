
#lab_8-5.py

def indexed_names(names):
    
    result = [f"{i}: {name}" for i, name in enumerate(names)]
    return result


test_names1 = ["John", "Jane", "Bob"]
test_names2 = ["bill", "joe", "Charlie"]

print("Test case 1:", indexed_names(test_names1)) 
print("Test case 2:", indexed_names(test_names2))  
