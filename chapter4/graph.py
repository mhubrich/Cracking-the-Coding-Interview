# Simple implementation of a graph that is used for other exercises

class Node:
    def __init__(self, value):
        self.value = value
        self.marked = False
        self.children = []

    def __str__(self):
        return '{node}: [{children}]'.format(node=str(self.value),
                                             children=', '.join([str(n.value) for n in self.children]))

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
    
    def __str__(self):
        return '\n'.join([str(n) for n in self.nodes])


def example_graph():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    a.children = [b, c, e]
    b.children = [a, d, e]
    c.children = [a, f, g]
    d.children = [b, e]
    e.children = [a, b, d]
    f.children = [c]
    g.children = [c]
    return Graph([a, b, c, d, e, f, g])