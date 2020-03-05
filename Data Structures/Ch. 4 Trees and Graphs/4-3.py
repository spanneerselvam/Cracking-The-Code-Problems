"""
4-3: Given a sotred (increasing order) array, write an algorithm to create bst with minimal height
"""
class BST:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.height = 0
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
        #Prints left, root, right
        if self.left != None:
            self.left.printInOrder()
        print(self.data)
        if self.right != None:
            self.right.printInOrder()
    def printPreOrder(self):
        #Prints Root, Left, Right
        print(self.data)
        if self.left != None:
            self.left.printPreOrder()
        if self.right != None:
            self.right.printPreOrder()
    def printPostOrder(self):
        #Prints Left, Right, root
        if self.left != None:
            self.left.printPostOrder()
        if self.right != None:
            self.right.printPostOrder()
        print(self.data)




arr = [1,3,4,5,9,8,2,7,6]
arr.sort()
index=len(arr)//2
arr[index]
a = BST(arr[index])
arr.remove(arr[index])
a.printPreOrder()
for x in arr:
    a.insert(x)
a.printPostOrder()
