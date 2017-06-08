class Node(object):
    """Node in a linked list."""

    def __init__(self, data, species):
        self.data = data
        self.next = None
        self.species = species

    def __repr__(self):
        return '<Node:{} Species: {}>'.format(self.data, self.species)


class LinkedList(object):
    """Linked List using head and tail"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data, species):
        """Add node with data to end of list."""

        new_node = Node(data, species)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node_by_index(self, index):
        """Remove node with given index"""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

            >>> ll = LinkedList()
            >>> ll.add_node('Eli', 'dog')
            >>> ll.add_node('Owen', 'cat')

            >>> ll.print_list()
            Eli dog
            Owen cat
        """

        current = self.head
        while current:
            print current.data, current.species
            current = current.next

    def enqueue(self, data, species):
        """Enqueues any animal into the FIFO shelter.
            >>> ll = LinkedList()
            >>> ll.enqueue('Eli', 'dog')
            >>> ll.enqueue('Owen', 'cat')
            >>> ll.print_list()
            Eli dog
            Owen cat

        """

        new_animal = Node(data, species)
        if not self.head:
            self.head = new_animal
            self.tail = new_animal
        else:
            self.tail.next = new_animal
            self.tail = new_animal

    def dequeue_any(self):
        """Dequeues the oldest(first in) animal at shelter. Can be either dog or cat.
            >>> ll = LinkedList()
            >>> ll.enqueue('Eli', 'dog')
            >>> ll.enqueue('Owen', 'cat')
            >>> ll.dequeue_any()
            <Node:Eli Species: dog>

        """
        adopted = self.head
        self.head = self.head.next
        return adopted

    def dequeue_dog(self):
        """Dequeues the dog that came into the shelter first.
            >>> ll = LinkedList()
            >>> ll.enqueue('Oscar', 'cat')
            >>> ll.enqueue('Eli', 'dog')
            >>> ll.enqueue('Owen', 'cat')
            >>> ll.dequeue_dog()
            <Node:Eli Species: dog>
        """

        prev = None
        current = self.head
        while current.species != "dog":
            prev = current
            current = current.next
        prev.next = current.next.next
        return current

    def dequeue_cat(self):
        """Dequeues the cat that came into the shelter first.
            >>> ll = LinkedList()
            >>> ll.enqueue('Eli', 'dog')
            >>> ll.enqueue('Oscar', 'cat')
            >>> ll.enqueue('Owen', 'cat')
            >>> ll.dequeue_cat()
            <Node:Oscar Species: cat>
        """

        prev = None
        current = self.head
        while current.species != "cat":
            prev = current
            current = current.next
        prev.next = current.next.next
        return current




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
