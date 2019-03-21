"""
    Because dictionaries are mutable, you need to be aware of aliasing.
    Whenever two variables refer to the same dictionary object, changes
    to one affect the other. For example, opposites is a dictionary t
    hat contains pairs of opposites.
"""
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])
