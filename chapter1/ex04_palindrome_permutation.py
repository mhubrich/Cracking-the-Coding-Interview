########################################################################################################
# Exercise 1.4                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a        #
# palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation  #
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.  #
########################################################################################################
from collections import defaultdict


# A palindrome has at most one character with odd frequency (because both halfs of the palindrome are
# mirrored, except for the middle character if the length of the string is odd).
# This approach uses a (default) dict to count character frequencies of the given string and returns
# False if there are more than one odd frequencies, True otherwise.
def palindrome_permutation(string):
    d = defaultdict(int)
    for s in string:
        d[s] += 1
    # First, we map all dict values to 0 (even) or 1 (odd) using the modulus operator.
    # Then we filter the result on only odd numbers (all of the 1s).
    # Finally, sum all remaining 1s and return False if there is more than one.
    return False if sum(filter(lambda x: x > 0, map(lambda x: x % 2, d.values()))) > 1 else True


if __name__ == '__main__':
    strings = ['tactcoa', 'atcocta', 'ataocta']
    for s in strings:
        print('Is {s} a permutation of a palindrome? {result}'.format(s=s, result=palindrome_permutation(s)))