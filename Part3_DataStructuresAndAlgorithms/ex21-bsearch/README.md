# Ex21: Binary Search

```
% python3 -m cProfile -s cumtime test_bsearch.py | grep .py   
        1    0.000    0.000    0.001    0.001 test_bsearch.py:1(<module>)
        1    0.000    0.000    0.001    0.001 bsearch.py:1(<module>)
        1    0.000    0.000    0.000    0.000 dllist.py:1(<module>)
        1    0.000    0.000    0.000    0.000 bstree.py:1(<module>)
...
        1    0.000    0.000    0.000    0.000 bstree.py:1(BSTreeNode)
        1    0.000    0.000    0.000    0.000 dllist.py:13(DoubleLinkedList)
        1    0.000    0.000    0.000    0.000 bstree.py:39(BSTree)
        1    0.000    0.000    0.000    0.000 dllist.py:1(DoubleLinkedListNode)
```