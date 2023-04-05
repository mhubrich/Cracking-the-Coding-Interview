########################################################################################################
# Exercise 3.4                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks                #
########################################################################################################

# Implementation of an ordinary Stack (helper class)
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack is empty.')
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def peek(self):
        if self.isEmpty():
            raise IndexError('Stack is empty.')
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
    
    # Implemented to make prints during testing/debugging easier
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.stack.__str__()


# MyQueue has two stacks, where the first stack is used to add items,
# and the second stack is used to remove and peek at items.
class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    # Transfer existing items to stack 1 (if not done already) and push new item there
    def add(self, item):
        self.__assert__()
        if self.stack1.isEmpty() and not self.stack2.isEmpty():
            self.__transfer__(self.stack2, self.stack1)
        self.stack1.push(item)
    
    # Transfer existing items to stack 2 (if not done already) and pop there
    def remove(self):
        self.__assert__()
        if not self.stack1.isEmpty() and self.stack2.isEmpty():
            self.__transfer__(self.stack1, self.stack2)
        return self.stack2.pop()

    # Transfer existing items to stack 2 (if not done already) and peek there
    def peek(self):
        self.__assert__()
        if not self.stack1.isEmpty() and self.stack2.isEmpty():
            self.__transfer__(self.stack1, self.stack2)
        return self.stack2.peek()
    
    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()
    
    # Transfers all items from stack s1 to stack s2 in reverse order
    def __transfer__(self, s1, s2):
        while not s1.isEmpty():
            s2.push(s1.pop())
    
    # At any given time, at most one stack can contain items
    def __assert__(self):
        assert (self.stack1.isEmpty() and self.stack2.isEmpty()) or \
               (self.stack1.isEmpty() and not self.stack2.isEmpty()) or \
               (not self.stack1.isEmpty() and self.stack2.isEmpty()), \
               'Both stacks contain items.'
    
    # Implemented to make prints during testing/debugging easier
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Stack 1: ' + str(self.stack1) + ', Stack 2: ' + str(self.stack2)


if __name__ == '__main__':
    queue = MyQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    print('Added 4 items: ' + str(queue))
    queue.peek()
    print('Peeked: ' + str(queue))
    queue.remove()
    queue.remove()
    print('Removed 2 items: ' + str(queue))
    queue.add(5)
    queue.add(6)
    print('Added 2 items: ' + str(queue))
    queue.remove()
    queue.remove()
    print('Removed 2 items: ' + str(queue))
