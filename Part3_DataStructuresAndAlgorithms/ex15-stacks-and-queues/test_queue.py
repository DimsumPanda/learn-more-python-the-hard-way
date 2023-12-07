from queue import Queue

def test_push():
    line = Queue()
    line._invariant()
    assert line.count() == 0
    line.push("Alice")
    assert line.count() == 1
    assert line.first() == "Alice"
    line._invariant()
    line.push("Bob")
    assert line.count() == 2
    line._invariant()
    line.dump("\nAfter test_push:")

def test_unshift():
    line = Queue()
    line.push("Alice")
    line.push("Bob")
    line.push("Cat")
    line.dump("\nBefore Alice unshift:")
    assert line.unshift() == "Alice"
    line._invariant()
    line.dump("\nAfter Alice unshift:")
    assert line.unshift() == "Bob"
    line._invariant()
    line.dump("\nAfter Bob unshift:")
    assert line.unshift() == "Cat"
    line.dump("\nAfter Cat unshift:")
    line._invariant()
    assert line.unshift() == None
    line._invariant
    

def test_first():
    line = Queue()
    line.push("Alice")
    assert line.first() == "Alice"
    line.push("Bob")
    assert line.first() == "Alice"
    line.push("Cat")
    assert line.first() == "Alice"
    line.unshift()
    assert line.first() == "Bob"

def test_last():
    line = Queue()
    line.push("Alice")
    assert line.last() == "Alice"
    line.push("Bob")
    assert line.last() == "Bob"
    line.push("Cat")
    assert line.last() == "Cat"
    line.unshift()
    assert line.last() == "Cat"