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
for line in fileref:
    print(line.strip("\n"))

fileref.close()
