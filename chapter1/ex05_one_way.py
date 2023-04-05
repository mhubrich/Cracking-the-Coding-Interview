########################################################################################################
# Exercise 1.5                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# One Away: There are three types of edits that can be performed on strings: insert a character,       #
# remove a character, or replace a character. Given two strings, write a function to check if they are #
# one edit (or zero edits) away.                                                                       #
########################################################################################################

def one_away(a, b):
    if len(a) - len(b) == 1:  # if potentially character removed from `b`, i.e. inserted into `a`
        return check_insert(b, a)
    if len(a) - len(b) == 0:  # if potentially character replaced in `b`
        return check_replace(a, b)
    if len(a) - len(b) == -1: # if potentially character inserted to `b`
        return check_insert(a, b)
    return False

# Checks if one character can be inserted into string `a` to yield string `b`.
# Assumes that string `b` is longer than string `a` by 1.
def check_insert(a, b):
    i, j = 0, 0
    while(i < len(a) and j < len(b)):
        if a[i] != b[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True

# Checks if strings `a` and `b` differ by exactly one character.
# Assumes that both strings have equal length.
def check_replace(a, b):
    edit = False
    for x, y in zip(a, b):
        if x != y:
            if edit:
                return False
            edit = True
    return True


if __name__ == '__main__':
    test_cases = [
        ['', ''],
        ['a', 'a'],
        ['a', 'b'],
        ['a', 'aaaaaaa'],
        ['abcd', 'abcd'],
        ['abcd', 'abce'],
        ['abcd', 'abdc'],
        ['abcd', 'dcba'],
        ['abcd', 'abc'],
        ['abcd', 'bcd'],
        ['abcd', 'acd'],
        ['abcd', 'adc'],
        ['abc', 'abcd'],
        ['abc', 'aabc'],
        ['abc', 'abcc']
    ]
    for (a, b) in test_cases:
        print("{a} -> {b} = {c}".format(a=a, b=b, c=one_away(a,b)))
