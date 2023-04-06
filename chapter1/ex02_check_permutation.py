########################################################################################################
# Exercise 1.2                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. #
########################################################################################################
from collections import defaultdict


# Uses a (default) dict to count character frequencies in both strings.
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    d = defaultdict(int)
    for s in s1:
        d[s] += 1
    for s in s2:
        d[s] -= 1
        if d[s] < 0:
            return False
    return True


if __name__ == '__main__':
    strings = ['apple', 'dog', 'god', 'odd']
    for x in strings:
        for y in strings:
            print('Is {x} a permutation of {y}? {result}'.format(x=x, y=y, result=check_permutation(x, y)))