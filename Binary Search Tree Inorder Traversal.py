
class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

rt = node(4)
l,r = node(2), node(5)
ll , lr = node(1) , node(3)
rr = node(6)

rt.left = l
rt.right = r
l.left = ll
l.right = lr
r.right = rr

def inorder_traversal(root):
    if root is None: return
    inorder_traversal(root.left)
    print(root.value , end=" ")
    inorder_traversal(root.right)

inorder_traversal(rt)