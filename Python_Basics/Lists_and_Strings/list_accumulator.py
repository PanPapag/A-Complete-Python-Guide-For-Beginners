nums = [3, 5, 8]
accum = []

for w in nums :
    x = w**2
    accum.append(x)
    print(accum)

print("Total accumulator: ", accum)

# For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for w in verbs:
    ing.append(w + "ing")
print(ing)

# Overwrite the list numbs so that each of the original numbers are increased by 5.
numbs = [5, 10, 15, 20, 25]
for index in range(len(numbs)):
    numbs[index] += 5
print(numbs)
