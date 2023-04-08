########################################################################################################
# Exercise 4.3                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the      #
# nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).             #
########################################################################################################
from binarytree import tree


# Helper class to `LinkedList`.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

# Simple implementation of a linked list.
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return ' -> '.join([str(x) for x in self])


# Returns a list of linked lists of all the nodes at each depth level.
# Kicks off the recursion
def get_list_of_depths(tree):
    list = []
    _get_list_of_depths(tree, list, 0)
    return list

# Implementation of DFS to iterate through each node in the tree. 
# It passes down a counter for the level and adds nodes to linked lists accordingly.
def _get_list_of_depths(root, list, level):
    if root == None: # We reached the end of the tree
        return
    
    if len(list) == level: # We have not seen this level yet and therefore create a new list
        list.append(LinkedList())
    
    list[level].add(root.value) # Add node to list, and recursively visit the left and right subtree
    _get_list_of_depths(root.left, list, level+1)
    _get_list_of_depths(root.right, list, level+1)


if __name__ == '__main__':
    my_tree = tree(height=4)
    print(my_tree)
    list = get_list_of_depths(my_tree)
    for level, x in enumerate(list, 1):
        print('Level {level}: {x}'.format(level=level, x=x))
