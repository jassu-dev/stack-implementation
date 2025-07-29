🧱 Stack Implementation Using Linked List in Python
Stacks are a fundamental data structure in computer science, operating on the LIFO (Last In, First Out) principle. This means that the last element added is the first one to be removed—like stacking plates in a kitchen.
🧩 Structure Overview
This implementation builds a stack using a linked list by defining three classes:
🔹 Node Class
Each node represents a single item in the stack.
class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


- value: stores the data.
- next: points to the next node (below it in the stack).
🔹 LinkedList Class
Serves as the base class with a head pointer indicating the top of the stack.
class LinkedList():
    def __init__(self):
        self.head = None


🔹 Stack Class
Inherits from LinkedList and provides all stack operations:
- isEmpty(): Checks if the stack is empty.
- push(value): Adds an element to the top of the stack.
- pop(): Removes and returns the top element.
- peek(): Returns the top element without removing it.
- delete(): Clears the entire stack.
- __str__(): Represents the stack as a string for printing.
🛠️ Sample Execution
a = Stack()
a.push(4)
a.push(10)
a.push(50)
print(a)          # Outputs: 50-->10-->4
print(a.peek())   # Outputs: 50


✅ Summary
Using a linked list ensures dynamic memory usage—ideal for situations where you don't know the number of elements in advance. It avoids overflow issues that can occur with fixed-size arrays. This implementation is simple, extendable, and clean for stack operations.
