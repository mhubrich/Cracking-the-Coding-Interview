########################################################################################################
# Exercise 4.1                                                                                         #
# ---------------------------------------------------------------------------------------------------- #
# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a      #
# route between two nodes.                                                                             #
########################################################################################################
from qqueue import Queue
from graph import example_graph


# Implements BFS to check if t can be reached from s.
def isConnected(s, t):
    queue = Queue()
    s.marked = True
    queue.enqueue(s)

    while(not queue.is_empty()):
        node = queue.dequeue()
        if node == t:
            return True
        for child in node.children:
            if not child.marked:
                node.marked = True
                queue.enqueue(child)
    
    return False


# Helper class for testing in main (sets all nodes in graph to unmarked)
def _reset(graph):
    for n in graph.nodes:
        n.marked = False


if __name__ == '__main__':
    graph = example_graph()
    print(graph)
    for s in graph.nodes:
        for t in graph.nodes:
            _reset(graph)
            print('Is {s} connected to {t}? {result}'.format(s=s.value, t=t.value,
                                                             result=isConnected(s, t)))