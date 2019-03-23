# Composition

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)

class PaperBook(Book):

    def __init__(self, title, author, num_pages):
        Book.__init__(self, title, author)
        self.num_pages = num_pages

class EBook(Book):

    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size

class Libray:

    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def getNumBooks(self):
        return len(self.books)

my_book = Book("The Odyssey", "Homer")
print(my_book)

my_paper_book = PaperBook("The Odyssey", "Homer", 500)
print(my_paper_book)

my_ebook = EBook("The Odyssey", "Homer", 2)
print(my_ebook)

adl = Libray()
adl.addBook(my_book)
adl.addBook(my_paper_book)
adl.addBook(my_ebook)
print(adl.getNumBooks())

# Overriding
"""
    If a method is defined for a class, and also defined for its parent class,
    the subclass’ method is called and not the parent’s.
    This follows from the rules for looking up attributes that you saw in the 
    previous section.
"""
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "grumpy; leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "randomly annoyed"
        else:
            return "happy"

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

c1 = Cat("Fluffy")
d1 = Dog("Astro")

c1.boredom = 1
print(c1.mood())
c1.boredom = 3
for i in range(10):
    print(c1.mood())
print(d1.mood())
