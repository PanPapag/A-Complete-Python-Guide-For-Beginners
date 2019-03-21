fruit = ["banana", "apple", "cherry"]
print("Initial fruits: ", fruit)

fruit[0] = "pear"
fruit[-1] = "cherry"
print("Mutated fruits: ", fruit)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
print("Initial list: ", alist)
mut = ['x', 'y']

alist[1:3] = mut                # for index 1 up to 3 (without 3) replace
                                #  alist[index] with mut
print("Mutated list: ", alist)

# e.g a way to delete items from a list is to Mutate them with empty alist
alist[1:3] = []
print("Delete items 'x' and 'y': ", alist)

greeting = "Hello world"
new_greeting = "J" + greeting[1:]
print(greeting) # same as it was
print(new_greeting)

phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"
print(excited_phrase_complete)
