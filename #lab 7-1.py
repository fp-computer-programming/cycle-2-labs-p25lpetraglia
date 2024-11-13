#lab 7-1
#lp

my_row = ["Alice", "Bob"]


my_row[len(my_row):] = ["Logan"]


my_row2 = my_row


print("my_row2:", my_row2)


del my_row[1]


print("my_row after deletion:", my_row)
print("my_row2 after deletion:", my_row2)
