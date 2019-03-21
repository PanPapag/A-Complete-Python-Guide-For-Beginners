from string import ascii_lowercase

f = open('olympics.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0
    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

for letter in ascii_lowercase:
    if letter in x:
        print(letter + ": " + str(x.get(letter)) + " occurrences")
    else :
        print(letter + ": 0 occurrences")

f.close()
