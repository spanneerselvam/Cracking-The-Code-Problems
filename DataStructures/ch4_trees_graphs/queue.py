"""
Implementation of Queue data structure. This is FIFO (First In First Out).
We can use a list as the base of our Stack class as seen below
"""
class Queue:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def length(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []
    def display(self):
        return self.items
    def pop(self):
        if not self.is_empty():
            del self.items[0] #del deletes at a specific index
            return self.items
    def peek(self):
        if not self.is_empty():
            return self.items[0]
q = Queue()
print(q.is_empty())
q.push(1)
q.push(2)
q.push(3)
print(q.display())
print(q.peek())
q.pop()
print(q.display())
print(q.peek())
