class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def _insert(self, node, key):
    if node is None:
      return Node(key)

    if key < node.key:
      node.left = self._insert(node.left, key)
    elif key > node.key:
      node.right = self._insert(node.right, key)

    return node

  def printParents(self):
    print('Printing parent of each node')
    self._printParent(self.root, None)

  def _printParent(self, node, parent):
    if node is not None:
      if parent is None:
        print(node.key, '-> Root')
      else:
        print(node.key, '->', parent.key)

      self._printParent(node.left, node)
      self._printParent(node.right, node)
  
  def printLeafNodes(self):
    print('Printing leaf nodes:')
    self._printLeafNodes(self.root)

  def _printLeafNodes(self, node):
    if node is not None:
      if not node.left and not node.right:
        print('Leaf node:', node.key)

      self._printLeafNodes(node.left)
      self._printLeafNodes(node.right)
  
  def countEdges(self):
    total_edges = self._countEdges(self.root)
    print('Total edges in the binary tree:', total_edges)

  def _countEdges(self, node):
    if node is None:
      return 0
    
    total = 0
    
    if node.left:
      total += 1 + self._countEdges(node.left)
    if node.right:
      total += 1 + self._countEdges(node.right)

    return total
  
tree = BinaryTree()

tree.insert(10)
tree.insert(15)
tree.insert(17)
tree.insert(5)
tree.insert(9)
tree.insert(4)
tree.insert(16)


tree.printParents()
tree.printLeafNodes()
tree.countEdges()