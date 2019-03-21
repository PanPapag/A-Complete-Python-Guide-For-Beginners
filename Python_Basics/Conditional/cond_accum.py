s = "what if we went to the zoo"
vowels = ['a', 'e', 'i', 'o', 'u']
x = 0
for i in s :
    if i in vowels :
        x += 1
print("Number of vowels: ",x)

"""
    For each string in the list words, find the number
    of characters in the string. If the number of characters
    in the string is greater than 3, add 1 to the variable
    num_words so that num_words should end up with
    the total number of words with more than 3 characters.
"""

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for word in words :
    if(len(word) > 3) :
        num_words += 1

"""
    For each word in words, add ‘d’ to the end of the word
    if the word ends in “e” to make it past tense. Otherwise,
    add ‘ed’ to make it past tense. Save these past tense
    words to a list called past_tense.
"""
words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words :
    if word[len(word) - 1] == 'e' :
        past_tense.append(word + 'd')
    else :
        past_tense.append(word + 'ed')

print(past_tense)
