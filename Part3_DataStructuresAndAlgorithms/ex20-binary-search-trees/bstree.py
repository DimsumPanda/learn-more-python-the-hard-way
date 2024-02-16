class BSTreeNode(object):
    
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.parent = parent
        self.value = value

    # find the minimum value in a branch
    def find_minimum(node):
        while node:
            if node.left:
                node = node.left
            else:
                return node
        return None

    def __repr__(self):
        leftVal = self.left.value if self.left else None
        rightVal = self.right.value if self.right else None
        parentVal = self.parent.value if self.parent else None
        return f"[{self.key}, {self.value}, {repr(parentVal)}, {repr(leftVal)}, {repr(rightVal)}]"

class BSTree(object):

    def __init__(self):
        self.root = None

    def get(self, key):
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None
    
    def set(self, key, value):
        node = self.root
        while node:
            if key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = BSTreeNode(key, value, node)
                    break
            elif key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = BSTreeNode(key, value, node)
                    break
            else:
                node.value = value


    def replace_node_in_parent(self, node):
        # set the successor
        successor = self.find_minimum(node.right)
        node.key = successor.key

    def delete(self, key):
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            elif key == node.key:
                if node.left and node.right:
                    # if both are not empty
                    print("do something")
                    successor = self.find_minimum(node.right)
                    node.key = successor.key
                elif node.left:
                    # if node only had a left child
                    deleted_val = node.value
                    node.value = node.left.value
                    node.left = node.left.left
                    node.right = node.left.right
                    node.left.parent = node
                    node.right.parent = node
                    return deleted_val
                elif node.right:
                    deleted_val = node.value
                    node.value = node.right.value
                    node.left = node.right.left
                    node.right = node.right.right
                    # parent should stay the same.
                    node.left.parent = node
                    node.right.parent = node
                    return deleted_val
                else:
                    if key < node.parent:
                        node.parent.left = None
                    else:
                        node.parent.right = None
            else:
                return None
            
    def list(self):
        node = self.root
        print(node)
        while node:
            if node.left:
                node_left = node.left
                while node_left:
                    print(node_left)
                    if node_left