# Implementation of a simple linked list.
# Offers functions: add, add_first, add_values, iterator.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            self.add_values(values)
    
    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)

    def add_first(self, value):
        self.head = Node(value, self.head)
    
    def add_values(self, values):
        for v in values:
            self.add(v)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __str__(self):
        return ' -> '.join([str(x) for x in self])