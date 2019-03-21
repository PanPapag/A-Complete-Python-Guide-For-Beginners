# Ex1 : Write a function named total that takes a list of integers as input,
#       and returns the total value of all those integers added together.

def total(lst) :
    sum = 0
    for num in lst :
        sum += num
    return sum

# Ex2 : Write a function called count that takes a list of numbers as input
#       and returns a count of the number of elements in the list.

def count(lst) :
    return len(lst)
