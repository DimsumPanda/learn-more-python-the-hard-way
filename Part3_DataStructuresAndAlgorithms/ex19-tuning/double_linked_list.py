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
        if self.begin == None:
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin
        elif self.begin == self.end:
            node = DoubleLinkedListNode(obj, self.begin, None)
            self.begin = node
            self.end.prev = node
        else:
            node = DoubleLinkedListNode(obj, self.begin, None)
            old_begin_node = self.begin
            old_begin_node.prev = node
            self.begin = node
    
    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        # if there are no nodes
        if self.begin:
            unshift_node_value = self.begin.value
            # if there is only one node
            if self.begin == self.end:
                self.begin = None
                self.end = None
            else:
                self.begin = self.begin.next
                self.begin.prev = None
            return unshift_node_value
        else:
            return None
    
    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly 
        inside remove(). It should take a node, and detach it from the 
        list, whether the node is at the front, end or in the middle."""
        if node == self.begin:
            self.unshift()
        elif node == self.end:
            self.pop()
        elif node.prev and node.next:
            # If it has a prev node and there's a node after this particular node,
            # Skip over the current node by updating the prev and next of 
            # surrounding nodes
            next_node = node.next
            node.prev.next = next_node
            next_node.prev = node.prev
        else:
            # do nothing if the node doesn't exist in the list
            pass

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        index = 0
        while node:
            if node.value == obj:
                self.detach_node(node)
                return index
            else:
                index += 1
                node = node.next
        return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value if self.begin else None
        
    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value if self.end else None
    
    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0

        while node:
            count += 1
            node = node.next

        return count
    
    def get(self, index):
        """Get the value at index."""
        node = self.begin
        for i in range(0,index+1):
            if i == index and node:
                return node.value
            elif node:
                node = node.next
            else:
                return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        node = self.begin
        print(mark)
        while node:
            print(f'{repr(node)}')
            node = node.next
    
    def to_list(self):
        node = self.begin
        result = []
        while node:
            result.append(node)
            node = node.next
        return result

    def _invariant(self):
        if self.begin == None:
            assert self.begin == self.end
        else:
            assert self.begin.prev == None
            assert self.end.next == None
