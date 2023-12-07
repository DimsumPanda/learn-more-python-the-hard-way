class QueueNode(object):

    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt
    
    def __repr__(self):
        nval = self.next.value if self.next else None
        pval = self.prev.value if self.prev else None
        return f'[{self.value},{repr(pval)},{repr(nval)}]'
    
class Queue(object):

    def __init__(self):
        self._head = None
        self._tail = None

    def push(self, obj):
        """Node is added to the end."""
        
        if self._head:
            node = QueueNode(obj, self._tail, None)
            self._tail.next = node
            self._tail = node
        else:
            node = QueueNode(obj)
            self._head = node
            self._tail = node

    def unshift(self):
        """Node is removed from the head of the line."""
        if self._head:
            old_head = self._head
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                self._head = self._head.next
                self._head.prev = None
            return old_head.value
        else:
            return None
        
    def first(self):
        """Return the value of the first node in the Queue"""
        return self._head.value
    
    def last(self):
        """Return the last value in the Queue"""
        return self._tail.value
    
    def count(self):
        """Count the number of nodes in queue"""
        count = 0
        node = self._head
        while node:
            count += 1
            node = node.next
        return count
    
    def dump(self, mark="---"):
        """Debugging print statements"""
        print(mark)
        node = self._head
        while node:
            print(node)
            node = node.next

    def _invariant(self):
        if self._head:
            self._head.prev == None
            self._tail.next == None
        else:
            assert self._head == self._tail

