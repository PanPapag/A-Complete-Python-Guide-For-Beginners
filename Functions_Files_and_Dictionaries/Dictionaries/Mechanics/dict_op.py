inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory)

del inventory['pears']      # deletes a <key,value>
print(inventory)

inventory['apples'] = 10    # change value associated with key apples
print(inventory)

inventory['bananas'] = inventory['bananas'] * 2
print(inventory)

num_items = len(inventory)
print("Items in inventory: ", num_items)
