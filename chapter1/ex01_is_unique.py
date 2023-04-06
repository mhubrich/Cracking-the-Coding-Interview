########################################################################################################
# Exercise 1.1                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you    #
# cannot use additional data structures?                                                               #
########################################################################################################

# Uses a set to check if a given string consists of unique characters.
# Alternatively, we could have used a hashtable (dictionary) instead of a set.
def is_unique(string):
    letters = set()
    for s in string:
        if s in letters:
            return False
        letters.add(s)
    return True

# Uses two for-loops to check if a given string consists of unique characters.
def is_unique_vanilla(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


if __name__ == '__main__':
    strings = ['apple', 'banana', 'fruit']

    print('=== Tests using set implemention ===')
    for s in strings:
        print('Is {s} unqiue? {x}'.format(s=s, x=is_unique(s)))
    
    print('=== Tests using vanilla implemention ===')
    for s in strings:
        print('Is {s} unqiue? {x}'.format(s=s, x=is_unique_vanilla(s)))