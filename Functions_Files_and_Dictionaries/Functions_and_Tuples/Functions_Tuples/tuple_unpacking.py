julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

name, surname, birth_year, movie, movie_year, profession, birth_place = julia

print(name)
print(surname)
print(movie)

# (a, b, c, d) = (1, 2, 3) # ValueError: need more than 3 values to unpack

def add(x, y):
    return x + y

print(add(3, 4))

z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked
# print(add(z)) # this line causes an error


# use tuple unpacking for cleaner code
d = {"k1": 3, "k2": 7, "k3": "some other value"}

for k, v in d.items():
    print("key: {}, value: {}".format(k, v))


def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)
