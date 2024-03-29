class BSTreeNode(object):
    
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.parent = parent
        self.value = value

    # find the minimum value in a branch
    def find_minimum(self):
        node = self
        while node.left:
            node = node.left
        return node

    def replace_child(self, child):
        """Given a child, it will find the child, move it's value to here, then remove it.
        Copied from wikipedia to solve it quicker.
        """
        if self.parent:
            # if the node is the parent's left child
            if self == self.parent.left:
                self.parent.left = child
            # if the node is the parent's right child
            else:
                self.parent.right = child
        
        # if the node has a child, replace the child's parent with the node's parent
        if child:
            child.parent = self.parent

    def __repr__(self):
        leftVal = self.left.value if self.left else None
        rightVal = self.right.value if self.right else None
        parentVal = self.parent.value if self.parent else None
        return f"[key: {self.key}, value:{self.value}, parent: {repr(parentVal)}, leftVal: {repr(leftVal)}, rightVal: {repr(rightVal)}]"

class BSTree(object):

    def __init__(self):
        self.root = None

    def get(self, key):
        """Get the value for the node at a given key."""
        
        if not self.root:
            return None
        
        # start at the root
        node = self.root
        while node:
            if node.key == key:
                return node.value
            elif node.left == None and node.right == None:
                return None
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                assert False, "Should not happen."

        return None
    
    def set(self, key, value):
        """Sets the key to the given value, replace any existing value."""
        
        # start at the root
        if self.root == None:
            self.root = BSTreeNode(key, value)
        else:
            node = self.root

            while node:
                if node.key == key:
                    node.value = value
                    break
                elif node.left == None and node.right == None:
                    # add a new node to the left or right depending on equality
                    if key < node.key:
                        node.left = BSTreeNode(key, value, parent=node)
                    else:
                        node.right = BSTreeNode(key, value, parent=node)
                    break
                    
                elif key < node.key:
                    if node.left:
                        node = node.left
                    else:
                        node.left = BSTreeNode(key, value, node)
                        break
                elif key >= node.key:
                    if node.right:
                        node = node.right
                    else:
                        node.right = BSTreeNode(key, value, node)
                        break
                else:
                    assert False, "Should not happen."

    def _delete(self, key, node):
        """Deletes the given key from the data structure."""

        assert node, "Invalid node given."

        # Uses recursion
        if key < node.key:
            self._delete(key, node.left)
        elif key > node.key:
            self._delete(key, node.right)
        else:
            if node.left and node.right:
                successor = node.find_minimum()
                node.key = successor.key
                self._delete(successor.key, successor)
            elif node.right:
                if self.root == node:
                    self.root = node.right
                else:
                    node.replace_child(node.right)
            elif node.left:
                if self.root == node:
                    self.root = node.left
                else:
                    node.replace_child(node.left)
            else:
                if self.root == node:
                    self.root = None
                else:
                    node.replace_child(None)

    def delete(self, key):
        if self.root:
            self._delete(key, self.root)
            
    def _list(self, node, indent=0):
        """List the elements in the tree."""
        
        assert node, "Invalid node given."

        if node:
            print(" " * indent, node.key, "=", node.value)

            if node.left:
                print(" " * indent, "<", end="")
                self._list(node.left, indent+1)
            if node.right:
                print(" " * indent, ">", end="")
                self._list(node.right, indent+1)

    def list(self, start=""):
        print("\n\n----", start)
        self._list(self.root)