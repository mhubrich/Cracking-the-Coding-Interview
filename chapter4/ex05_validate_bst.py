########################################################################################################
# Exercise 4.5                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Validate BST: Implement a function to check if a binary tree is a binary search tree.                #
########################################################################################################
from binarytree import tree, bst


# Checks if a given binary tree is a binary search tree.
# The recursive algorithm checks if all left descendents <= node < all right descendents for all nodes.
def is_BST(node, min_value=None, max_value=None):
    # When leaf nodes are reached -> stop recursion
    if node == None:
        return True
    
    # Compare node to current minimum and maximum values
    if (min_value and node.value < min_value) or (max_value and node.value >= max_value):
        return False
    
    # Update minimum and maximum values and test left and right subtrees
    return min(is_BST(node.left, min_value=min_value, max_value=node.value),
               is_BST(node.right, min_value=node.value, max_value=max_value))


if __name__ == '__main__':
    my_tree = tree(height=4)
    print(my_tree)
    print('Is tree a binary search tree? {result}'.format(result=is_BST(my_tree)))

    my_tree = bst(height=4)
    print(my_tree)
    print('Is tree a binary search tree? {result}'.format(result=is_BST(my_tree)))