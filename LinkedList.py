class Node:
    """A node with a key (value) and a next pointer"""

    def __init__(self, key, next_=None):
        self.key = key
        self.next_ = next_

    def __str__(self):
        return str(self.key)


class LinkedList:
    """A singly-linked list with only a head pointer"""

    def __init__(self):
        self.head = None

    def __str__(self):
        s = 'head'
        node = self.head
        while True:
            if node is None:
                break
            s += ' -> {}'.format(node)
            node = node.next_
        return s

    def push(self, key):
        """Add a node to the front of the list"""
        node = Node(key)
        node.next_ = self.head
        self.head = node

    def pop(self):
        """Return the node from the front of the list"""
        if self.empty():
            return None
        node_to_pop = self.head
        self.head = node_to_pop.next_
        return node_to_pop

    def empty(self):
        """Return True if list is empty"""
        return self.head is None

    def contains(self, key):
        """Return True if list contains a node whose key is `key`"""
        node = self.head
        while True:
            if node is None:
                break
            if node.key == key:
                return True
            node = node.next_
        return False
