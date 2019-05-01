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

"""
The for loop below produces a list of numbers greater than 10. Below the
given code, use list comprehension to accomplish the same thing.
Assign it the the variable lst2. Only one line of code is needed.
"""

L = [12, 34, 21, 4, 6, 9, 42]
lst = []
for x in L:
    if x > 10:
        lst.append(x)
print(lst)

lst2 = [x for x in L if x > 10]
print(lst2)

"""
Write code to assign to the variable compri all the values of the key name
in any of the sub-dictionaries in the dictionary tester. Do this using a
list comprehension.
"""

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
import json
inner_list = tester['info']
print(json.dumps(inner_list, indent=2))
compri = [d['name'] for d in inner_list]
print(compri)
