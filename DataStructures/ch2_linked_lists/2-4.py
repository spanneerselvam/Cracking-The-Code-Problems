#2-4: Write code to partition a linked list around a value x, such that all nodes less than x
#   come before all nodes greater than or equal to x
#Building Linked List in Python

class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None #pointer to next node

class LinkedList:
    def __init__(self):
        self.head = Node() #head node should always be available. Doesn't contain data and shouldn't be indexiable
        #place holder
    def append(self, data):
        """
        Given a data point, append new node to linked list.
        """
        new_node = Node(data)
        current_node = self.head
        while current_node.next!=None:
            current_node = current_node.next
        current_node.next = new_node #when we are at the last node, set it's pointer to point at the new Node
    def length(self):
        """
        Returns length of linked list
        """
        current_node = self.head
        size = 0
        while current_node.next!=None:
            size += 1
            current_node = current_node.next
        return size
    def display(self):
        """
        Displays all items in the linked list
        """
        elems = [] #create a list of elements we've seen
        current_node = self.head
        while current_node.next!=None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)
    def get(self, index):
        """
        Returns the data point at the given index in the linked list
        """
        if index >= self.length():
            print("ERROR")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index: return current_node.data
            current_index += 1
    def get_index(self, data):
        """
        Return the index at the given data point in the linked list
        """
        current_node = self.head
        current_index = 0
        while current_node.next != None:
            current_node = current_node.next
            if current_node.data == data:
                return current_index
            current_index += 1
        print("data doesn't exist")
        return None
    def erase(self, index):
        """
        Given the index, will erase the node in the linked list
        """
        if index >= self.length():
            print("ERROR")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1
    def delete(self, data):
        """
        Given the data point, will delete the node in the linked list
        """
        current_node = self.head
        current_index = 0
        index = self.get_index(data)
        while current_node.next != None:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1
    def insert_index(self, index, data):
        new_node = Node(data)
        if index >= self.length():
            print("ERROR")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = new_node
                new_node.next = current_node
                return
            current_index += 1

    def split(self, data):
        index = self.get_index(data)
        less_than = []
        greater_than = []
        current_node = self.head
        current_index = 0
        while current_node.next != None:
            current_node = current_node.next
            if current_node.data > data:
                greater_than.append(current_node.data)
            if current_node.data < data:
                   less_than.append(current_node.data)
            self.delete(current_node.data)
            current_index += 1
        for item in less_than:
            self.append(item)
        self.append(data)
        for item in greater_than:
            self.append(item)
    def sort(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
            self.delete(current_node.data)
        elems.sort()
        for item in elems:
            self.append(item)

a = LinkedList()
my_list = [8,4,3,2,1, 5,6,7]
for item in my_list:
    a.append(item)
a.display()
a.insert_index(2, 0)
a.insert_index(100, 1)
a.insert_index(5, 100)
a.display()
a.split(7)
a.display()
a.sort()
a.display()
