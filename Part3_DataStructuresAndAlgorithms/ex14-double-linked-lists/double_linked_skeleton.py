class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""

    def pop(self):
        """Removes the last item and returns it."""

    def shift(self, obj):
        """Actually just another name for push but from the beginning node."""
    
    def unshift(self):
        """Removes the first item (from begin) and returns it."""

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly 
        inside remove(). It should take a node, and detach it from the 
        list, whether the node is at the front, end or in the middle."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove."""

    def count(self):
        """Counts the number of elements in the list."""

    def get(self, index):
        """Get the value at index."""
    
    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""