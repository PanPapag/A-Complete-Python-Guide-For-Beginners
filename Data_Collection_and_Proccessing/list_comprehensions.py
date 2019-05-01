things = [2, 5, 9]

yourlist = [value * 2 for value in things]

print(yourlist)

def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things))))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])
