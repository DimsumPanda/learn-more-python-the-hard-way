import sys
from pathlib import Path

HERE = Path(__file__).parent
EX13_PATH = HERE.parents[1].joinpath('ex13-single-linked-lists')

# Add ex13 to current system path
sys.path.append(str(EX13_PATH))

from single_linked_list import SingleLinkedList

class Stack(object):

    def __init__(self):
        self.list = SingleLinkedList()

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        self.list.push(obj)

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        return self.list.pop()

    def top(self):
        """
        Returns the value of the node on the top of the stack, 
        i.e. the last book added.
        """
        return self.list.last()
    
    def count(self):
        """Counts the number of elements in the stack."""
        return self.list.count()

    def dump(self, mark):
        self.list.dump(mark)