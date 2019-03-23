city_names = ["Detroit", "Ann Arbor", "Pittsburgh", "Mars", "New York"]
population = [680250, 117070, 304391, 1683, 8406000]
states = ["MI", "MI", "PA", "PA", "NY"]

city_tuples = zip(city_names, population, states) # zip creates a list of tuples

class City():
    def __init__(self, n, p, s):
        self.name = n
        self.population = p
        self.state = s
    def __str__(self):
        return "{} {} (population: {})".format(self.name, self.population, self.state)

# A dumb way to create a list of instances of class City

#cities = []
#for city_tup in city_tuples:
#    name, pop, state = city_tup
#    city = City(name, pop, state) # Instance of the city class
#    cities.append(city)
#print(cities)

cities = [City(n, p, s) for n, p, s in city_tuples]
print(cities)

# Flexing way
#cities = [City(*t) for t in city_tuples]    # unpacking tuple using *
#print(cities)
