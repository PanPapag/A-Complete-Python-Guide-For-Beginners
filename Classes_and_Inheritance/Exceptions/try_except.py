try:
    items = ['a', 'b']
    print("This wil be printed")
    third = items[2]
    print("This won't print")
except:
    print("got an error")

try:
    x = 5
    y = x/0
    print("This won't print, either")
except:
    print("error 2")

print("continuing")
