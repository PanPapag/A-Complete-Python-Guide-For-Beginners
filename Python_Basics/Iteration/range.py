x = range(5)
print(type(x))
print(x)

print("range(10): ")
for i in range(5):
    print(i)

print("range(2,10): ")
for i in range(2, 10):
    print(i)

# Notice the casting of `range` to the `list`
lst1 = list(range(10))
lst2 = list(range(2, 10))
print(lst1)
print(lst2)

# Note: `range` function is already casted as `list` in the textbook
print(range(5))

numbers = list(range(0,41))
sum1 = 0
for anum in numbers:
    sum1 += anum

fruit = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruit)):
    print(n, fruit[n])
