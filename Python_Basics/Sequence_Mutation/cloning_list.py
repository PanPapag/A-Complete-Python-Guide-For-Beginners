"""
If we want to modify a list and also keep a copy of the original,
we need to be able to make a copy of the list itself, not just the reference.
This process is sometimes called cloning, to avoid the ambiguity of the word copy.

The easiest way to clone a list is to use the slice operator.

Taking any slice of a creates a new list. In this case the slice happens to consist of the whole list.
"""

a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)
