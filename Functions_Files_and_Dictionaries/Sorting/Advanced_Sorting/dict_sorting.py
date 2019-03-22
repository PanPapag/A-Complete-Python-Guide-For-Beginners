L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

print("Sorting by key")

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
y = sorted(d.keys())
for k in y:
    print("{} appears {} times".format(k, d[k]))

print("\nSorting by value")

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))

# Ex : Sort the following dictionary’s keys based on the value from highest
#       to lowest. Assign the resulting value to the variable sorted_values.

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
sorted_values = sorted(dictionary , key = lambda k: dictionary[k], reverse=True )
print()
print(dictionary)
