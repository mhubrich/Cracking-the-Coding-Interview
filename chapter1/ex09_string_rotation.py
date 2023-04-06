########################################################################################################
# Exercise 1.9                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# String Rotation: Assume you have a method isSubstring which checks if one word is a substring        #
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only   #
# one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").                         #
########################################################################################################

# Checks if s2 is a substring of s1
def isSubstring(s1, s2):
    return s2 in s1

# Checks if s2 is a rotation of s1
# It does it by concatenating s1 with itself and calling the isSubstring function
# Example: s1=erbottlewat, s1s1=erbottlewaterbottlewat, s2=waterbottle
def is_rotated(s1, s2):
    if len(s1) != len(s2):
        return False
    return isSubstring(s1 * 2, s2)


if __name__ == '__main__':
    s1 = 'erbottlewat'
    s2 = 'waterbottle'
    print('Is {s2} a rotation of {s1}? {result}'.format(s2=s2, s1=s1, result=is_rotated(s1, s2)))