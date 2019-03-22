def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum  = 0
    aNumber = 1
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))

print(sumTo(1000))

# Ex1 : Write a while loop that is initialized at 0 and stops at 15.
#       If the counter is an even number, append the counter to a list called eve_nums.

eve_nums = []
counter = 0
while counter <= 15:
    if counter % 2 == 0:
        eve_nums.append(counter)
    counter += 1

print(eve_nums)

# Ex2 : Below, we’ve provided a for loop that sums all the elements of list1.
#       Write code that accomplishes the same task, but instead uses a while loop.
#        Assign the accumulator variable to the name accum.


list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
for elem in list1:
    tot = tot + elem

idx = 0
accum = 0
while idx < len(list1):
    accum += list1[idx]
    idx += 1

print(tot == accum)
