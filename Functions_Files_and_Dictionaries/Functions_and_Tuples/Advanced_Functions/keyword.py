initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are:", x, y, z)

f(2, z = 10)
# f(10, x = 2) #Runtime error

# NOTE optional parameters should be after required ones
