fileref = open("olympics.txt","r")  # open file olympics.txt to read only

contents = fileref.read()           # is going to bring in the entire contents
                                    #of the file as a single string
print(contents[:100])

fileref.seek(0)                     # rewind fileref

lines = fileref.readlines()         # read line by line
print("File lines: ", len(lines))
for line in lines[:4]:              # each string in list lines has a '\n' in the end
    print(line.strip("\n"))         # and print() always print '\n', so use strip to avoid "\n\n"


# more pythonic way to read whole file
fileref.seek(0)                     # rewind fileref
number_of_lines = 0
for line in fileref.readlines():
    number_of_lines += 1
    print(line.strip("\n"))

fileref.close()

# Ex1 : Using the file school_prompt2.txt, find the number of characters
#       in the file and assign that value to the variable num_char

f = open("school_prompt2.txt", "r")
content = f.read()
num_char = len(content)
print("school_prompt2.txt number of characters: ", num_char)
f.close()

# Ex2 : create a string called first_forty that is comprised of
#       the first 40 characters of emotion_words2.txt.

f = open("emotion_words2.txt", "r")
content = f.read()
first_forty = content[:40]
print("emotion_words2.txt first 40 characters are : ", first_forty)
f.close()
