import test

# Return value test
def square(x):
    return x*x

test.testEqual(square(3), 9)

# Side effect test

def update_counts(letters, counts_d):
    for c in letters:
        counts_d[c] = 1
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1

counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
test.testEqual(counts['a'], 6)
# 1 more occurrence of b, so 3 in all
test.testEqual(counts['b'], 3)
