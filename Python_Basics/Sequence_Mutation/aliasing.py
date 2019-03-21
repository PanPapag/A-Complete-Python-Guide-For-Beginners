"""
    Because the same list has two different names, a and b, we say that
    it is aliased. Changes made with one alias affect the other. In the codelens
    example below, you can see that a and b refer to the same list after
    executing the assignment statement b = a.
"""

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)
