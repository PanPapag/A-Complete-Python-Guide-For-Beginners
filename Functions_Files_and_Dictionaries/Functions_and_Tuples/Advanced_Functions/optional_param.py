def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2,[1]))


print(int("100"))
print(int("100", 10))   # same thing, 10 is the default value for the base
print(int("100", 8))    # now the base is 8, so the result is 1*64 = 64
