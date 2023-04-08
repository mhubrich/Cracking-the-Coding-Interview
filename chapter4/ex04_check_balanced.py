########################################################################################################
# Exercise 4.4                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of      #
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of  #
# any node never differ by more than one.                                                              #
########################################################################################################
from binarytree import tree


# Checks if given tree is balanced or not.
# Kicks off recursion.
def is_balanced(tree):
    return _is_balanced(tree)[1]

# Recursively travels to the leaf nodes and increases a height counter on the way back up.
# If the heights of the left or right subtrees differ by more than 1 for any node the 
# recursion bubbles up a False value.
def _is_balanced(root):
    if root == None:
        return 0, True
    
    height_left, balanced_left = _is_balanced(root.left)
    height_right, balanced_right = _is_balanced(root.right)

    if abs(height_left - height_right) > 1:
        return max(height_left, height_right)+1, False
    else:
        return max(height_left, height_right)+1, min(balanced_left, balanced_right)


if __name__ == '__main__':
    my_tree = tree(height=4)
    print(my_tree)
    print('Is tree balanced? {result}'.format(result=is_balanced(my_tree)))