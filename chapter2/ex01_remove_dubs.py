########################################################################################################
# Exercise 2.1                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Remove Dups: Write code to remove duplicates from an unsorted linked list.                           #
# FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?                    #
########################################################################################################
from linked_list import LinkedList


# Removes duplicated values in a given linked list.
# It does so by storing all already seen values in a hashtable (set).
def remove_dups(linked_list):
    values = set()
    previous = None
    for node in linked_list:
        if node.value in values:
            previous.next = node.next
        else:
            values.add(node.value)
            previous = node
    return linked_list

# Removes duplicated values in a given linked list.
# It does so by running through the linked list with two pointers: one pointer iterates through
# the linked list and the other one checks all subsequent nodes for duplicates.
def remove_dups_vanilla(linked_list):
    for node in linked_list:
        runner = node
        while runner.next:
            if runner.next.value == node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
    return linked_list


if __name__ == '__main__':
    print('=== Implementation with Hashtable ===')
    linked_list = LinkedList([4,8,2,4,8,1,9,5,4,8,3])
    print('Original: {list}'.format(list=linked_list))
    print('Dups removed: {list}'.format(list=remove_dups(linked_list)))

    print('=== Implementation without Hashtable ===')
    linked_list = LinkedList([4,8,2,4,8,1,9,5,4,8,3])
    print('Original: {list}'.format(list=linked_list))
    print('Dups removed: {list}'.format(list=remove_dups_vanilla(linked_list)))