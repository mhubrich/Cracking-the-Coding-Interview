########################################################################################################
# Exercise 3.5                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use #
# an additional temporary stack, but you may not copy the elements into any other data structure       #
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.      #
########################################################################################################

# Implementation of an ordinary Stack (helper class)
class Stack:
    def __init__(self, *items):
        self.stack = list(items)

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


# Sorts `stack_main` in ascending order (smallest on top) using `stack_temp` as helper
# It does it by iteratively popping an item from `stack_main` and sorting it into `stack_temp` in descending order
def sort_stack(stack_main, stack_temp):
    assert stack_temp.isEmpty(), 'Temporary stack is not empty.'
    while not stack_main.isEmpty():
        sorted_insert(stack_main.pop(), stack_temp, stack_main)
    transfer(stack_temp, stack_main)

# Inserts `item` into `stack_main` in descending order (biggest on top) using `stack_temp` as helper
def sorted_insert(item, stack_main, stack_temp):
    while not stack_main.isEmpty() and item < stack_main.peek():
        stack_temp.push(stack_main.pop())
    stack_main.push(item)

# Transfers all items from stack s1 to stack s2 in reverse order
def transfer(s1, s2):
    while not s1.isEmpty():
        s2.push(s1.pop())


if __name__ == '__main__':
    stack_main = Stack(5, 3, 2, 7, 7, 8, 6)
    stack_temp = Stack()
    print('Unsorted: ' + str(stack_main))
    sort_stack(stack_main, stack_temp)
    print('Sorted: ' + str(stack_main))
