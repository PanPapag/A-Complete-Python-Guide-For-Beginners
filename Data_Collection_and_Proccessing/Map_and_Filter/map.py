def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
print("Initial: ", things)
things3 = tripleStuff(things)
print("Triple: ", things3)
things4 = quadrupleStuff(things)
print("Quadruple: ",things4)

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))

#EX1 :  Using map, create a list assigned to the variable greeting_doubled
# that doubles each element in the list lst.

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = list(map(lambda value: 2*value, lst))
print(lst)
print(greeting_doubled)

#EX2: Below, we have provided a list of strings called abbrevs.
# Use map to produce a new list called abbrevs_upper that contains all
# the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper = list(map(lambda value: value.upper(), abbrevs))
print(abbrevs)
print(abbrevs_upper)
