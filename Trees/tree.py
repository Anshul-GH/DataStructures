class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print('Found it !!')
            return self

        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)

        print('Not found !!')

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(1000)

# print(node.right.data)
# print(node.right.right.data)

myTree = Tree(node, 'My Tree')

# print(myTree.name)
# print(myTree.root.left.data)
# print(myTree.root.right.right.data)

# print(myTree.root)

found = myTree.root.search(1000)
if found:
    print(found.data)

found = myTree.root.search(10000)
if found:
    print(found.data)