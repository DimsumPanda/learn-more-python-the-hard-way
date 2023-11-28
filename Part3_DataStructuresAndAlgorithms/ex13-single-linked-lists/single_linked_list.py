class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        """This line checks if the node has a next node (self.next). 
        If it does, it assigns the value of the next node to nval; 
        otherwise, it assigns None."""
        # nval = self.next and self.next.value or None
        nval = self.next.value if self.next else None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):
    
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            # if it's a new list, then set this newly pushed node
            # as the begin and end of this list
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node
            assert self.begin != self.end

        assert self.end.next == None

    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            # Start with the first node's "next" node
            # This will stop at the third to last node
            # Second to last node will be (node.next == self.end)
            while node.next != self.end:
                node = node.next # traverse until node = second to last node
            assert self.end != node
            # Save the previous end node to return
            old_end_node_value = node.next.value
            # Set the end to second to last node
            self.end = node
            # returns the original next value.
            self.end.next = None
            
            return old_end_node_value
        
    def shift(self, obj):
        """Another name for push but from the beginning node."""
        node = SingleLinkedListNode(obj, None)
        # If this is the beginning of the list
        if self.begin == None:
            self.begin = node
            self.end = node
        else:
            # Get the self.begin and set it as the new node
            # set the next to the previously begin node
            node.next = self.begin
            self.begin = node
            assert self.begin != self.end

        assert self.end.next == None
        assert self.begin != None

    def unshift(self):
        """Removes the first item and returns it."""
        # Set the next node of the begin node to be the begin node
        unshift_node_value = None
        if self.begin == None:
            pass
        elif self.begin.next:
            unshift_node_value = self.begin.value
            self.begin = self.begin.next
        else:
            unshift_node_value = self.begin.value
            self.begin = self.end = None
        return unshift_node_value

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        index = 0
        if self.begin == None:
            pass
        else:
            current_node = self.begin
            # Loop through the nodes and remove any nodes that match the value of the object.
            while current_node:
                # Remove the node if the value matches the object
                if current_node.value == obj:
                    # Check if the value matches the begin node, if it does, unshift the list
                    if current_node == self.begin:
                        self.unshift()
                    # Check if the value matches the end node, if it does, pop the list
                    elif current_node == self.end:
                        self.pop()
                    return index
                # Check the next node and see if it matches.
                if current_node.next == obj:
                    if current_node.next.next:
                        current_node.next = current_node.next.next
                    else:
                        current_node.next = None
                    return index + 1
                current_node = current_node.next
                index += 1
        return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

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
        if self.begin == None:
            return None
        else:
            node = self.begin
            for i in range(0, index+1):
                if i == index:
                    return node.value
                elif node.next:
                    node = node.next
                else:
                    return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        node = self.begin
        print(f"{mark}:")
        while node:
            print(node.value, end=" ")
            node = node.next
        print("\n")

##########################################################################
# The following commented out lines is exploratory testing of the 
# SingleLinkedListNode class.
##########################################################################

# listNode1 = SingleLinkedListNode("A", None)
# print(listNode1.value)              # A
# print(listNode1.next)               # None

# listNode2 = SingleLinkedListNode("B", listNode1)
# print(listNode2.value)              #B
# print(listNode2.next.value)         #A

# listNode3 = SingleLinkedListNode("C", listNode2)
# print(listNode3.value)              #C
# print(listNode3.next.value)         #B
# print(listNode3.next.next.value)    #A

# print("Print Nodes:")
# print(listNode1)                    # [A:None]
# print(listNode2)                    # [B:'A']
# print(listNode3)                    # [C:'B']

