########################################################################################################
# Exercise 4.2                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an         #
# algorithm to create a binary search tree with minimal height.                                        #
########################################################################################################
from binarytree import Node # Used solely for pretty prints during testing


# Creates a minimal BST by kicking off the recursion.
def minimal_BST(array):
    return _minimal_BST(array, 0, len(array)-1)

# Recursive algorithm to create a minimal BST.
# The idea is to take the middle element of the given array as the root node, and recursively
# call the algorithm with the left side of the array for the left child, and the right side
# of the array for the right child.
def _minimal_BST(array, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = _minimal_BST(array, start, mid-1)
    node.right = _minimal_BST(array, mid+1, end)
    return node


if __name__ == '__main__':
    array = [9, 12, 14, 17, 19, 23, 50, 54, 67, 72, 76]
    print(minimal_BST(array))