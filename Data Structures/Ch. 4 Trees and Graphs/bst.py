class BST:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
    def insert(self, value):
        #Use recursion to insert
        if self.data == None:
            self.data = value
        #If value is smaller than root, insert to left
        if value <= self.data:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        #If value is greater than data, insert to right
        if value > self.data:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if self.data == None:
            return False
        if value == self.data:
            return True
        if value < self.data:
            if self.left == None:
                return False
            else:
                self.left.contains(value)
        if value > self.data:
            if self.right == None:
                return False
            else:
                self.right.contains(value)
    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.data)
        if self.right != None:
            self.right.printInOrder()

a = BST(2)
a.insert(1)
a.insert(3)
a.insert(0)
a.printInOrder()
