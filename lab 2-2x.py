# author lp 9/10/2024
a = 3
b = a
print("Value of a:", a)
print("Value of b:", b)
# a is 3 because  its assigned directly.
# b is also 3 because it was set b equal to a which was 3 at the time of assignment.
a = 7
print("Value of a after update:", a)
print("Value of b after update:", b)
# a is now 7 because we updated its value.
# b remains 3 because when we initially assigned b = a it was given the value of a before
# Since integers are immutable in Python, changing a later does not affect b.