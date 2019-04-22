nested1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
print([nested1[0]]) # prints first sub-list
print(len(nested1[0])) # prints length of first sub-list
nested1.append(['i'])
print(nested1)
for index,l in enumerate(nested1):
    print(index, l)

nested1[0].append("test") # append to first sub-list
print(nested1)

print(nested1[1][0])    # from the second list print first item ('d')

nested1[1] = [1, 2, 3]    # second sub-list is now the list [1, 2, 3]
print(nested1)

# EX1: 1. 2. Using indexing, retrieve the string ‘willow’ from the list
#and assign that to the variable plant.

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]
plant = data[7][0][0]
