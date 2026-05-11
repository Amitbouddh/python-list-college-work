# Tuple

my_tuple = (1, "apple", 3.14)

print(my_tuple)
print(type(my_tuple))

# Access elements
print(my_tuple[0])
print(my_tuple[1])

# Empty tuple
my_tuple2 = ()
print(my_tuple2)

# -------------------

# Lists

list1 = [1, 3, 5, 7]
list2 = [1, 2, 3, 5, 6]

# Add lists
list3 = list1 + list2

print(list3)

# Indexing
print(list3[0])
print(list3[1])

# Slicing
print(list3[1:5])

# Reverse
print(list3[::-1])

# Add element
list3.append(100)

print(list3)

# Remove element
list3.remove(100)

print(list3)

# Length
print(len(list3))

# Loop
for i in list3:
    print(i)