from stack import Stack

def test_push():
    books = Stack()
    books.push("Falling Up")
    assert books.top().value == "Falling Up"
    books.push("Where the Sidewalk Ends")
    assert books.top().value == "Where the Sidewalk Ends"
    assert books.top().next.value == "Falling Up"
    books.dump("After 2 books pushed to stack")

def test_pop():
    books = Stack()
    books.push("Falling Up")
    books.push("Where the Sidewalk Ends")
    books.push("The Light in the Attic")
    books.dump("After 3 books pushed to stack:")
    assert books.top().value == "The Light in the Attic"
    assert books.pop() == "The Light in the Attic"
    assert books.top().value == "Where the Sidewalk Ends"
    books.dump("After first book popped:")
    assert books.pop() == "Where the Sidewalk Ends"
    books.dump("After second book popped:")
    assert books.top().value == "Falling Up"
    assert books.pop() == "Falling Up"
    books.dump("After last book popped:")
    assert books.top() == None

def test_top():
    books = Stack()
    assert books.top() == None
    books.push("Falling Up")
    assert books.top().value == "Falling Up"
    assert books.top().next == None
    books.push("Where the Sidewalk Ends")
    assert books.top().value == "Where the Sidewalk Ends"
    assert books.top().next.value == "Falling Up"

def test_count():
    books = Stack()
    assert books.count() == 0
    books.push("Falling Up")
    assert books.count() == 1 
    assert books.top().value == "Falling Up"
    books.push("Where the Sidewalk Ends")
    assert books.count() == 2
    assert books.top().value == "Where the Sidewalk Ends"
    assert books.top().next.value == "Falling Up"
    books.push("The Light in the Attic")
    assert books.count() == 3
    books.dump("After 3 Books pushed:")
    books.pop()
    assert books.count() == 2
    books.pop()
    assert books.count() == 1
    books.pop()
    assert books.count() == 0
