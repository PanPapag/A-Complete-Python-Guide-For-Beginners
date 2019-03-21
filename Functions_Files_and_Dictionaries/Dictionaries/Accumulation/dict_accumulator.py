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
