inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

lks = list(inventory.keys())
lvs = list(inventory.values())
lis = list(inventory.items())

print(lks)
print(lvs)
print(lis)

# A more pythonic way to iterate over a dictionary
for k in inventory:
    print("Got",k,"that maps to",inventory[k])

print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print("We have : ", inventory['bananas'], " bananas")
else:
    print("We have no bananas")

print(inventory.get("apples"))          # inventory['apples']
print(inventory.get("cherries"))        # returns none if cherries not in inventory, cannot use inventory['cherries']

print(inventory.get("cherries",0))      # returns 0 if cherries not in inventory, cannot use inventory['cherries']
