########################################################################################################
# Exercise 3.3                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.   #
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some      #
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be            #
# composed of several stacks and should create a new stack once the previous one exceeds capacity.     #
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack                 #
# (that is, pop() should return the same values as it would if there were just a single stack).        #
########################################################################################################

# Implementation of an ordinary Stack (helper class)
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack is empty.')
        self.size -= 1
        return self.stack.pop()

    def push(self, data):
        self.size += 1
        self.stack.append(data)

    def peek(self):
        if self.isEmpty():
            raise IndexError('Stack is empty.')
        return self.stack[-1]

    def isEmpty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size

    # Implemented to make prints during testing/debugging easier
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.stack.__str__()


# SetOfStacks inherits from Stack, i.e. it is a Stack of Stacks with limited capacity
class SetOfStacks(Stack):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
    
    # Pop item from last stack, and if this stack becomes empty, remove it from set of stacks
    def pop(self):
        if self.isEmpty():
            raise IndexError('SetOfStacks is empty.')
        data = self.stack[-1].pop()
        if self.stack[-1].isEmpty():
            self.stack.pop()
            self.size -= 1
        return data

    # Push item to last stack, and if this stack exeeds its capacity, add new stack to set
    def push(self, data):
        if self.isEmpty() or len(self.stack[-1]) >= self.capacity:
            self.stack.append(Stack())
            self.size += 1
        self.stack[-1].push(data)

    # Peek at item in last stack
    def peek(self):
        if self.isEmpty():
            raise IndexError('SetOfStacks is empty.')
        return self.stack[-1].peek()


if __name__ == '__main__':
    stacks = SetOfStacks(3)
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    print('Pushed 3 items: ' + str(stacks))
    stacks.push(4)
    stacks.push(5)
    stacks.push(6)
    stacks.push(7)
    print('Pushed 4 items: ' + str(stacks))
    stacks.pop()
    print('Popped 1 item: ' + str(stacks))
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    stacks.pop()
    print('Popped 5 items: ' + str(stacks))
    stacks.pop()
    print('Popped 1 item: ' + str(stacks))
