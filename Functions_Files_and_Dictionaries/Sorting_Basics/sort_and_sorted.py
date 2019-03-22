L1 = [1, 7,  4, -1, 2]
L2 = ["cherry", "apple", "blueberry"]

L1.sort()
print(L1)

L2.sort()
print(L2)

L3 = ["cherry", "apple", "blueberry"]

L4 = sorted(L3) # does not mutates List
print(L4)
print(L3) # unchanged

L3.sort()   # mutates list List
print(L3)
print(L3.sort())

print(sorted("Apple"))

# NOTE We can use sorted() in any sequence
