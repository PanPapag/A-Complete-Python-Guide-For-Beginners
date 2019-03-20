# The overall syntax is for <loop_var_name> in <sequence>:
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")

for achar in "Hello World":
    print(achar)

fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:     # by item
    print(afruit)

# By using the enumerate function, we can print out a counter that tells us the position of an item in a list. 
for counter, item in enumerate(['apple', 'pear', 'apricot', 'cherry', 'peach']):
    print(counter, item)
