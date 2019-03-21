def double(y):
    y = 2 * y

def changeit(lst):
    lst[0] = "New one"

y = 5
print("Initial y: ",y)
double(y)
print("Doubled y: ",y)

mylist = ["lets", "see", "what", "will", "change"]
print("Initial list: ",mylist)
changeit(mylist)
print("Changed list: ",mylist)
