class Queue(object):
    """Simple FIFO queue, implemented using a list.

    This is a non-optimal way to make a queue--but it's just here as a demo
    of using a queue. Much better would be to use a linked list or
    collections.deque.
    """

    def __init__(self):
        self._data = []

    def enqueue(self, node):
        """Add item to end of queue."""

        self._data.append(node)

    def dequeue(self):
        """Remove item from start of queue and return."""

        return self._data.pop(0)

    def is_empty(self):
        """Is the queue empty?"""

        return not self._data

    def peek(self):
        """Return (but don't pop!) first item from start."""

        return self._data[0]

class Node(object):
    def __init__(self, data, adjacent=None):
        self.data = data
        if adjacent is None:
            self.adjacent = set()
        else:
            self.adjacent = adjacent

class Connections(object):
    """
    >>> node1 = Node("Amelia")
    >>> node2 = Node("Eli")
    >>> node3 = Node("Alex")
    >>> node4 = Node("George")
    >>> connections = Connections()
    >>> connections.add_nodes([node1, node2, node3, node4])
    >>> connections.add_route(node1, node2)
    >>> connections.add_route(node2, node3)
    >>> connections.add_route(node3, node4)
    >>> connections.are_connected(node1, node4)
    True


    """
    def __init__(self):
        self.nodes = set()

    def add_node(self, node):
        """Add a node to our graph"""

        self.nodes.add(node)

    def add_nodes(self, nodes):
        """Add a list of nodes to our graph"""

        for node in nodes:
            self.nodes.add(node)

    def add_route(self, node1, node2):
        node1.adjacent.add(node2)
        node2.adjacent.add(node1)

    def are_connected(self, node1, node2):
        to_visit = Queue()
        to_visit.enqueue(node1)
        seen = set()
        seen.add(node1)

        while not to_visit.is_empty():
            current = to_visit.dequeue()
            if current == node2:
                return True
            else:
                for node in current.adjacent - seen:
                    to_visit.enqueue(node)
                    seen.add(node)
        return False

if __name__ == '__main__':
    import doctest
    
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
