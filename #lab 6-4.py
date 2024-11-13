#lab 6-4
#lp

subjects = ["English", "Math", "History"]


subjects.append("Science")


index_of_math = subjects.index("Math")


subjects.sort()


subjects_copy = subjects.copy()


subjects_copy.sort(reverse=True)


print("Original subjects list (alphabetical order):", subjects)
print("Index of 'Math' in the original list:", index_of_math)
print("Copy of subjects list (reverse alphabetical order):", subjects_copy)
