a = "I have had an apple in my desk before!"
print(a.count("e"))    # k - sensitive, counts only 'e' not uppercase e
print(a.count("ha"))

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))

music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))

# ΝΟΤΕ: when index searching for sth that do not exist gives error
