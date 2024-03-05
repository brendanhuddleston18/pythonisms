class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for value in reversed(collection):
                self.insert(Node(value))


    def insert(self, value):
        self.head = Node(value, self.head)
    
    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()
    
    def __str__(self):
        output = ""

        for node in self:
            output += f"[ {node} ] -> "

        return output + "None"



class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_