class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

a_stack = Stack()
a_stack.push("hola")
a_stack.push("mundo")
pop = a_stack.pop()
pop2 = a_stack.pop()
pop3 = a_stack.pop()
print(pop)
print(pop2)
print(pop3)

