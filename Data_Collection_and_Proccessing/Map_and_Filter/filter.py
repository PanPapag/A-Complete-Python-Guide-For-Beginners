def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print("manual: ", keep_evens([3, 4, 6, 7, 0, 1]))

def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print("filter: ", keep_evens([3, 4, 6, 7, 0, 1]))

"""
Write code to assign to the variable filter_testing all the elements
in lst_check that have a w in them using filter.
"""

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = list(filter(lambda word: 'w' in word, lst_check))
print(lst_check)
print(filter_testing)
