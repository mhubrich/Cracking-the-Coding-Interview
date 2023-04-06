########################################################################################################
# Exercise 1.3                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string  #
# has sufficient space at the end to hold the additional characters, and that you are given the "true" #
# length of the string. (Note: If implementing in Java, please use a character array so that you can   #
# perform this operation in place.)                                                                    #
########################################################################################################

# Iterates through the array of characters and counts spaces
def count_spaces(char_array):
    count = 0
    for x in char_array:
        if x == ' ':
            count += 1
    return count

# Iterates through the array backwards and shifts characters accordingly
def URLify(char_array, length):
    spaces = count_spaces(char_array)
    for i in range(length-1, 0, -1):
        if spaces <= 0: # Stop early if no spaces left
            break
        if char_array[i] == ' ': # If space, insert '%20'
            spaces -= 1
            char_array[i+2*spaces] = '%'
            char_array[i+2*spaces+1] = '2'
            char_array[i+2*spaces+2] = '0'
        else: # If no space, move character backwards
            char_array[i+2*spaces] = char_array[i]
    return char_array


if __name__ == '__main__':
    s = 'Mr John Smith'
    char_array = list(s) + ['' for _ in range(4)]
    print(char_array)
    print(URLify(char_array, len(s)))