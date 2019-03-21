mylist = []             # creates an empty list

mylist.append(5)        # add a new item to the end of the list
mylist.append(27)
mylist.append(3)
mylist.append(10)
print(mylist)

mylist.insert(3, 5)     # insert, inserts the item wherever you tell it to.
                        # In this case, we're going to tell it to insert at position number one.
print(mylist)
print(mylist.count(5))  # count returns number of occurences of 12 's in this case

print(mylist.index(3))  # Index is a method, where we will pass in a value and it
                        # will tell us the position where that value can be found

mylist.reverse()        # reverse the list
print(mylist)

mylist.sort()           # Sort it's going to take the items in the list and just reorder them from smallest to biggest
print(mylist)

mylist.remove(5)         # remove, doesn't specify a position, it specifies a value. Remove only the first occurence
print(mylist)

last_item = mylist.pop()   # pop() removes the last item from the list
print(last_item)
print(mylist)
