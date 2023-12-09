import sys, os
from pathlib import Path

# Add ex14 to current system path
sys.path.insert(0, 'os.path.dirname')
part3_dir = Path(__file__).parents[2]
sys.path.append(os.path.join(part3_dir, 'ex14-double-linked-lists'))

from double_linked_list import DoubleLinkedList

class Queue(object):
    def __init__(self):
        self.list = DoubleLinkedList()

    def push(self, obj):
        """Node is added to the end."""
        self.list.push(obj)

    def unshift(self):
        """Node is removed from the head of the line."""
        return self.list.unshift()
    
    def drop(self):
        """Node is removed from the tail of the line. Someone gets out of line."""
        old_last = self.list.last()
        self.list.remove(old_last)
        return old_last

    def first(self):
        """Return the value of the first node in the Queue"""
        return self.list.first()
    
    def last(self):
        """Return the last value in the Queue"""
        return self.list.last()
    
    def count(self):
        """Count the number of nodes in queue"""
        return self.list.count()

    def dump(self, mark="---"):
        """Debugging print statements"""
        self.list.dump(mark)

    def _invariant(self):
        self.list._invariant()