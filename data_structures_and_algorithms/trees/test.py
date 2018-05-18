class Node:
    def __init__(self, key, parent_node = None):
        self.left = None
        self.right = None
        self.height = 0
        self.key = key
        self.parent = parent_node


o = Node(8)
o.left = Node(6, o)
o.left.right = Node(7, o.left)

node = o.left

r = node.right
p = node.parent
r.parent = p
p.left = r
r.left = node
node.parent = r
node.right = None
del node


node = o

l = node.left
p = node.parent
if p == None:
    l.parent = None
    l.right = node
    node.parent = l
    node.left = None
    
    del node
else:
    l.parent = p
    p.right = l
    l.right = node
    node.parent = l
    node.left = None
    del node

print(o.key)





