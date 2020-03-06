"""
Implementation of Stack data structure. This is LIFO (Last In First Out).
We can use a list as the base of our Stack class as seen below 
"""
class Stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def length(self):
        return len(self.items)
    def get_stack(self):
        return self.items
    def peek(self):
        if not self.is_empty():
            return self.items[self.length() - 1]
    def is_empty(self):
        return self.items == []
s = Stack()
print(s.is_empty())
print(s.peek())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.get_stack())
print(s.peek())
s.pop()
print(s.get_stack())
print(s.is_empty())
