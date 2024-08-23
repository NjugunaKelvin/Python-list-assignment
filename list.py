# Empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert value 15 on index 1(second position)
my_list.insert(1, 15)

# Extend list
my_list.extend([50, 60, 70])

# remove last element
my_list.pop()

# sort the list
my_list.sort()

# find & print index of the value 30
index_of_30 = my_list.index(30)

# print
print(my_list)
print(f"The index of 30 in my_list is: {index_of_30} ")