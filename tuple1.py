# Example 1: Creating and accessing a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) 
print(my_tuple[-1]) 

# Example 2: Trying to modify a tuple
my_tuple = (1, 2, 3, 4, 5)
try:
    my_tuple[0] = 10 
except TypeError:
    print("Tuples are immutable")