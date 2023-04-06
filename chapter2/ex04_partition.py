########################################################################################################
# Exercise 2.4                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x   #
# come before all nodes greater than or equal to x. If x is contained within the list, the values of x #
# only need to be after the elements less than x (see below). The partition element x can appear       #
# anywhere in the "right partition"; it does not need to appear between the left and right partitions. #
########################################################################################################
from linked_list import LinkedList


# Partitions a linked list around a value x.
# It does so by iterating through the linked list and moving smaller elements than x
# to the beginning of the list.
def partition(linked_list, x):
    node = linked_list.head
    while node.next:
        if node.next.value < x:
            # Remove n = node.next from linked list
            n = node.next
            node.next = n.next
            # Move n to the head
            n.next = linked_list.head
            linked_list.head = n
        else:
            node = node.next
    return linked_list


if __name__ == '__main__':
    linked_list = LinkedList([3, 5, 8, 5, 10, 2, 1])
    x = 5
    print('Original: {list}'.format(list=linked_list))
    print('Partition around {x}: {list}'.format(x=x, list=partition(linked_list, x)))