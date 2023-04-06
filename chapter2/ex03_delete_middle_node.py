########################################################################################################
# Exercise 2.3                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but        #
# the first and last node, not necessarily the exact middle) of a singly linked list, given only       #
# access to that node.                                                                                 #
########################################################################################################
from linked_list import LinkedList


# Deletes a given node from its linked list (all nodes but first or last).
# It does so by copying the value and pointer of the next node into the given node.
def delete_middle(node):
    if node is None or node.next is None:
        return False
    node.value = node.next.value
    node.next = node.next.next
    return True


if __name__ == '__main__':
    linked_list = LinkedList([1,2,3,4])
    print('Original: {list}'.format(list=linked_list))
    node = linked_list.head.next.next
    delete_middle(node)
    print('Delete 3rd node: {list}'.format(list=linked_list))