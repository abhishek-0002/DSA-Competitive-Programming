class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

	def insert(self,key):
		if self.key:
			if key < self.key:
				if self.left is None:
					self.left = Node(key)
				else:
					self.left.insert(key)
			elif key > self.key:
				if self.right is None:
					self.right = Node(key)
				else:
					self.right.insert(key)
			else:
				self.key = key

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print(self.key)
		if self.right:
			self.right.PrintTree()

root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)		