
class BinaryTree:
	def __init__(self, data = None):
		self.data = data
		self.right = None
		self.left = None
	def insert(self, value):
		if self.data == None:
			self.data = value
		elif self.data != None:
			if self.left == None:
				self.left = BinaryTree(value)
			elif self.right == None:
				self.right = BinaryTree(value)
			elif self.left != None:
				self.left.insert(value)
			else:
				self.right.insert(value)

	def printInOrder(self):
		if self.left != None:
			self.left.printInOrder()
		print(self.data)
		if self.right != None:
			self.right.printInOrder()

a = BinaryTree()
a.insert(1)
a.insert(2)
a.insert(3)
a.printInOrder()