def f(x):
    return x - 1

print(type(f))
print(f(3))

# or equivalently
lf = lambda x: x - 1
print(type(lambda x: x - 1))
print(type(lf))
print(lf(3))
