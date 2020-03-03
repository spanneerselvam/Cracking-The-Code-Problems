#2-5: Adding numbers in LinkedList

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
        """
        Given the data point and index, will insert new node at the given index
        """
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
        """
        Given a data point, will split linked list so everything less than
        will come before and everything greater than will come after
        [2, 1, 3, 4, 9, 6, 5, 7, 8] = split(4)
        """
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
        """
        Sorts all elements of list
        """
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
            self.delete(current_node.data)
        elems.sort()
        for item in elems:
            self.append(item)
    def concat_list(self, my_list=[], *args):
        result = ''
        for item in my_list:
            result += str(item)
        return result
    def addition(self):
        """
        Each node contains a single digit. Adding two different numbers and appending
        the result to the linked list
        """
        middle = int(self.length()//2)
        current_node = self.head
        current_index = 0
        less_than = []
        greater_than = []
        while current_node.next != None:
            current_node = current_node.next
            if current_index <= middle:
                less_than.append(current_node.data)
            else:
                greater_than.append(current_node.data)
            current_index += 1
        n1 = self.concat_list(less_than)
        n2 = self.concat_list(greater_than)
        self.append(int(n1)+int(n2))
        return int(n1)+int(n2)
    def reverse_addition(self):
        """
        Same as class method above, just reversed.
        """
        middle = int(self.length()//2)
        current_node = self.head
        current_index = 0
        less_than = []
        greater_than = []
        while current_node.next != None:
            current_node = current_node.next
            if current_index <= middle:
                less_than.append(current_node.data)
            else:
                greater_than.append(current_node.data)
            current_index += 1
        less_than.reverse()
        greater_than.reverse()
        n1 = self.concat_list(less_than)
        n2 = self.concat_list(greater_than)
        self.append(int(n1)+int(n2))
        return int(n1)+int(n2)

a = LinkedList()
my_list = [8,4,3,2,1, 5,6,7]
for item in my_list:
    a.append(item)
a.display()
print(a.addition())
a.display()
