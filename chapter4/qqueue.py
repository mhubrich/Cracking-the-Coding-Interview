# Helper class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# Simple implementation of a queue that utilizes a linked list.
# Enqueue adds to the tail, and dequeue removes and returns the head.
class Queue:
    def __init__(self):
        self.head = self.tail = None

    def is_empty(self):
        return self.head == None
    
    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = node.next
        if self.is_empty():
            self.tail = None
        return node.value

    def peek(self):
        return None if self.is_empty() else self.head.value
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __str__(self):
        return ' -> '.join(reversed([str(x) for x in self]))