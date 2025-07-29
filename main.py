class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
class LinkedList():
    def __init__(self):
        self.head = None
class Stack(LinkedList):
    def isEmpty(self):
        if(self.head == None):
            return True
        return False
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def __str__(self):
        str_ans = ""
        a = self.head
        while a:
            str_ans+=str(a.value)
            if(a.next != None):
                str_ans += "-->"
            a = a.next
        return str_ans
    def pop(self):
        node_value = self.head.value
        self.head = self.head.next
        return node_value
    def delete(self):
        self.head = None
    def peek(self):
        if(self.head != None):
            peek_value = self.head.value
            return peek_value
        else:
            print("Sorry LinkedList is Empty")
a = Stack()
a.push(4)
a.push(10)
a.push(50)
print(a)
print(a.peek())