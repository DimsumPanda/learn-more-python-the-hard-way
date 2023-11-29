class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        # nval = self.next and self.next.value or None
        nval = self.next.value if self.next else None
        # pval = self.prev and self.prev.value or None
        pval = self.prev.value if self.prev else None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        # Check if there are any nodes
        if self.begin == None:
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin
        else:
            node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = node
            self.end = node

    def pop(self):
        """Removes the last item and returns it."""
        if self.begin == None:
            return None
        elif self.begin == self.end:
            popped_value = self.end.value
            self.begin = None
            self.end = None
        else:
            popped_value = self.end.value
            new_end_node = self.end.prev
            self.end = new_end_node
            self.end.next = None
        return popped_value


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
        node = self.begin
        count = 0
        if self.begin == None:
            pass
        elif self.begin == self.end:
            count = 1
        else:
            count = 1
            while node != self.end:
                count += 1
                node = node.next
        return count
    
    def get(self, index):
        """Get the value at index."""
        node = self.begin
        for i in range(0,index):
            if node:
                node = node.next
        return node.value

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
    
    def _invariant(self):
        if self.begin == None:
            assert self.begin == self.end
        else:
            assert self.begin.prev == None
            assert self.end.next == None