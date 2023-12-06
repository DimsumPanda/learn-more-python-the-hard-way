class StackNode(object):

    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next.value if self.next else None
        return f"[{self.value}:{repr(nval)}]"
    
class Stack(object):

    def __init__(self):
        self._top = None

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        node = StackNode(obj, self._top)
        if self._top:
            self._top = node
            # Since this is a stack, the next node should be the book under top.
        else:
            self._top = node

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        if self._top:
            old_top = self._top
            new_top = self._top.next
            self._top = new_top
            return old_top.value
        else:
            return None

    def top(self):
        """Returns a *reference* to the first item, does not remove."""
        return self._top

    def count(self):
        """Counts the number of elements in the stack."""
        node = self._top
        count = 0
        while node:
            count +=1
            node = node.next
        return count

    def dump(self, mark="---"):
        """Debugging function that dumps the contents of the stack."""
        print(mark)
        node = self._top
        while node:
            print(f'{node}')
            node = node.next