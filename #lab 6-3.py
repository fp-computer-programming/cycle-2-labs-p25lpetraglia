#lab 6-3
#lp

colors = ["red", "blue", "green", "yellow"]


colors.extend(["purple", "orange", "pink"])


colors.append("brown")


colors.insert(3, "white")


colors_copy = colors.copy()


colors_copy.remove("green")


print("Original colors list:", colors)
print("Copy of colors list after removal:", colors_copy)
