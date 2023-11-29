from double_linked_list import DoubleLinkedListNode, DoubleLinkedList

def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    colors._invariant()
    assert colors.count() == 1
    colors.push("Ultrameraine Blue")
    assert colors.count() == 2
    colors._invariant()

def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors._invariant()
    colors.push("Alizarin")
    colors.push("Van Dyke")
    colors._invariant()
    assert colors.pop() == "Van Dyke"
    colors._invariant()
    assert colors.get(1) == "Alizarin"
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    colors._invariant()
    assert colors.pop() == None