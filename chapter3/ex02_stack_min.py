##################################################################################################
# Exercise 3.2                                                                                   #
# ---------------------------------------------------------------------------------------------- #
# Stack Min: How would you design a stack which, in addition to push and pop, has a function min #
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.          #                                                                    #
##################################################################################################

# Data in StackMin is wrapped by helper class `Item` which helps to keep track of minimum.
class StackMin:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack is empty.')
        return self.stack.pop().data

    # For every push operation, save the current minimum with the new Item
    def push(self, data):
        item = Item(data)
        if not self.isEmpty():
            min = self.min()
            item.min = min if min < data else data
        self.stack.append(item)

    def peek(self):
        if self.isEmpty():
            raise IndexError('Stack is empty.') 
        return self.stack[-1].data

    def isEmpty(self):
        return len(self.stack) == 0

    def min(self):
        if self.isEmpty():
            raise IndexError('Stack is empty.') 
        return self.stack[-1].min


class Item:
    def __init__(self, data):
        self.data = data
        self.min = data


if __name__ == '__main__':
    stack = StackMin()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(1)
    print('Pushed 2->3->4->1')
    print('Current min: {min}'.format(min=stack.min()))
    print('Popped {item}'.format(item=stack.pop()))
    print('Current min: {min}'.format(min=stack.min()))
