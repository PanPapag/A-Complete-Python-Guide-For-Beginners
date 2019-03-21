a = "banana"
b = "banana"

print("a = ", a, ", b = ", b, " ", a is b)
print("a id: ", id(a))
print("b id: ", id(b))

# An example with lists
"""
    alist and blist have equivalent values but do not refer to the same object.
    Because their contents are equivalent, alist == blist evaluates to True;
    because they are not the same object, alist is blist evaluates to False.
"""
alist = [81,82,83]
blist = [81,82,83]

print(alist is blist)

print(alist == blist)

print(id(alist))
print(id(blist))
