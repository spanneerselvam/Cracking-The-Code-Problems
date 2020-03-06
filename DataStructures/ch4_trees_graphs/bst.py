class BST:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.nodes = []
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
    def inOrderTraversal(self):
        if self.left != None:
            self.left.inOrderTraversal()
        self.nodes.append(self.data)
        if self.right != None:
            self.right.inOrderTraversal()
        return self.nodes
    def balance(self, nodes = [], *args):
        #nodes = self.inOrderTraversal()
        #nodes.sort()
        nodes.sort()
        split = len(nodes)//2
        b = BST(nodes[split])
        nodes.remove(nodes[split])
        rh = nodes[0:split]
        lh = nodes[split:len(nodes)]
        if len(rh) > 1:
            self.balance(rh)
        elif len(rh) == 1:
            for x in rh:
                b.insert(x)
        elif len(lh) > 1:
            self.balance(lh)

        elif len(lh) == 1:
            for x in lh:
                b.insert(x)
        return b
    def balance_tree(self):
        a = BST()
        nodes = self.inOrderTraversal()
        print(nodes)
        return self.balance(nodes)

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



b = BST()
a = BST(2)
a.insert(1)
a.insert(3)
a.insert(0)
b = a.balance_tree()
b.printInOrder()
"""
nodes = [1, 2, 4, 5, 3]
nodes.sort()
print(nodes)
split = len(nodes)//2
print(nodes[split])
nodes.remove(nodes[split])
print(nodes)
rh = nodes[0:split]
print(rh)
lh = nodes[split:len(nodes)]
print(lh)
"""