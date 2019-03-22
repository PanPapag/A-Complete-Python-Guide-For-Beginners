# # NOTE:
"""
    It is a little confusing that we are reusing the word key so many times.
    The name of the optional parameter is key. We will usually pass a parameter
    value using the keyword parameter passing mechanism.
    When we write key=some_function in the function invocation,
    the word key is there because it is the name of the parameter,
    specified in the definition of the sort function,
    not because we are using keyword-based parameter passingself.
"""

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

# or in reverse order
print(sorted(L1, reverse = True, key = absolute))

# Ex : Below, we have provided a list of strings called nums. Write a
#      function called last_char that takes a string as input, and returns only
#       its last character. Use this function to sort the list nums by the last
#       digit of each number, from highest to lowest, and save this as a new
#       list called nums_sorted.

nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(str):
    return str[-1]

nums_sorted = sorted(nums, key = last_char, reverse = True)
# or using lambda
nums_sorted_lambda = sorted(nums, key = lambda str : str[-1], reverse = True)

print(nums_sorted)
print(nums_sorted_lambda)
