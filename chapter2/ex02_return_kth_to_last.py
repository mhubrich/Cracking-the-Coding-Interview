########################################################################################################
# Exercise 2.2                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.  #
########################################################################################################
from linked_list import LinkedList


# Returns the kth to last element of a given linked list.
# It has two pointers which are exactly k nodes apart. When the second pointer is at the end 
# of the list, the first pointer is at the kth from last node.
def kth_to_last(linked_list, k):
    pointer1 = linked_list.head
    pointer2 = move(linked_list.head, k)
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

# Moves `node` by `k` places
def move(node, k):
    for _ in range(k):
        if node is None:
            raise IndexError('Node does not have {k} successors.'.format(k=k))
        node = node.next
    return node


if __name__ == '__main__':
    values = [1,2,3,4,5,6,7,8,9]
    linked_list = LinkedList(values)
    print('Linked List: {list}'.format(list=linked_list))
    for k, v in enumerate(values):
        print('{k} element from last: {result}'.format(k=k+1, result=kth_to_last(linked_list, k+1)))