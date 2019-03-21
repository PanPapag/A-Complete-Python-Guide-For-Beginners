# Ex1 : Provided is a string saved to the variable name sentence.
#       Split the string into a list of words, then create a dictionary that
#       contains each word and the number of times it occurs.
#       Save this dictionary to the variable name word_counts.

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

wlist = list(sentence.split())  # Split the string into a list of words

word_counts = {}                # creates an empty dictionary
for word in wlist :
    if word not in word_counts :
            # we have not seen this word before, so initialize a counter for it
            word_counts[word] = 0
    #whether we've seen it before or not, increment its counter
    word_counts[word] += 1
print(word_counts)

# Ex2 : The dictionary travel contains the number of countries within
#       each continent that Jackie has traveled to. Find the total number of
#       countries that Jackie has been to, and save this number to the
#       variable name total. Do not hard code this!

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0
for key in travel :
    total += travel[key]
print(total)

# Ex3 :  Create a dictionary called d that keeps track of all the characters
#        in the string placement and notes how many times each character was seen.
#       Then, find the key with the lowest value in this dictionary and assign
#       that key to min_value

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {} # start with an empty dictionary
for c in placement.strip():
    if c not in d:
        # we have not seen this character before, so initialize a counter for it
        d[c] = 0
    #whether we've seen it before or not, increment its counter
    d[c] = d[c] + 1

keys = list(d.keys())
min_value = keys[0]

for key in keys :
    if d[key] < d[min_value] :
        min_value = key

print(min_value)
