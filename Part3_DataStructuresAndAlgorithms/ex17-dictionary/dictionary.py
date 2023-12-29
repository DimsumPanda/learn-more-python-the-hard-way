import sys
from pathlib import Path

HERE = Path(__file__).parent
EX14_PATH = HERE.parent.joinpath('ex14-double-linked-lists')

# Add ex14 to current system path
sys.path.append(str(EX14_PATH))

from double_linked_list import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256):
        """Initializes a Map with the given number of buckets."""
        self.map = DoubleLinkedList()
        for i in range(0, num_buckets):
            # Map is a DoubleLInkedList
            # Here we are pushing another DoubleLinkedList
            # as a node.
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        """Given a key this will create a number and then convert it to an index 
        for the aMap's buckets."""
        # hash is a built-in python function that returns a hash value of an 
        # object if it has one
        # Then we are taking the modulus of the hash given the current count of 
        # the doublelinkedlist (map)
        return hash(key) % self.map.count()
    
    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        # set the bucket_id. 
        # bucket_id will be hash(key) % self.map.count()
        bucket_id = self.hash_key(key)
        # We are using the doubleLinkedList's get method to get the node aka
        # the doubleLinkedList at the bucket_id
        return self.map.get(bucket_id)
    
    def get_slot(self, key, default=None):
        """
        Returns either the bucket and node for a slot, or None, None
        """
        # bucket will be get_bucket (get the bucket id given the key)
        bucket = self.get_bucket(key)

        # if the bucket_id exists
        if bucket:
            # Each bucket is a double-linked-list
            node = bucket.begin
            # i = 0

            # Loop through the nodes in the "bucket" double-linked-list
            while node:
                # If the node value matches the key we are looking for
                #  return the bucket (the double_linked_list) and the node
                if key == node.value[0]:
                    return bucket, node
                # if not, keep iterating through the nodes
                else:
                    node = node.next
                    # i += 1

        # fall through for both if and while above
        return bucket , None
    
    def get(self, key, default=None):
        """Gets the value in a bucket for the given key, or the default."""
        # Given the key, you can get the bucket (the double-linked-list)
        # and the node
        # to get_slot, you need to find the bucket id of the key which may not exist.
        bucket, node = self.get_slot(key, default=default)
        # return just the node and its value
        # return node and node.value[1] or node
        return node.value[1] if node else node
    
    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""
    
        bucket, slot = self.get_slot(key)

        if slot:
            # the key exists, replace it
            slot.value = (key, value)
        else:
            # the key does not, append to create it
            bucket.push((key, value))

    def delete(self, key):
        """Deletes the given key from the Map."""
        # the bucket is a double-linked-list
        bucket = self.get_bucket(key)
        node = bucket.begin

        # Loop through the "bucket" aka double-linked-list until key == the 
        # node's key in the node's value tuple
        while node:
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break
            else:
                node = node.next

    def list(self):
        """Prints out what's in the Map."""
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next

