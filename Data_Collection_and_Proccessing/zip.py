L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = list(zip(L1, L2))
print(L3)

sumList = [x1 + x2 for x1, x2 in list(zip(L1,L2))]
print(sumList)

sumList2 = list(map(lambda x: x[0] + x[1], zip(L1, L2)))
print(sumList2)

"""
Below we have provided two lists of numbers, L1 and L2. Using zip and list
comprehension, create a new list, L3, that sums the two numbers if the number
from L1 is greater than 10 and the number from L2 is less than 5.
This can be accomplished in one line of code.
"""
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x1 + x2 for x1, x2 in list(zip(L1,L2)) if x1 > 10 and x2 < 5]
