from InorderTraversal import inorder_traversal

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

def find_inorder_succ(root):
    root = root.right
    while root.left:
        root = root.left
    return root


def delete(root,value):
    if root is None: return
    if root.value == value:

        if root.right is None and root.left is None:
            return None

        elif root.right is None and root.left is not None:
            return root.left

        elif root.right is not None and root.left is None:
            return root.right

        else:
            in_successor = find_inorder_succ(root)
            root.value = in_successor.value
            root.right = delete(root.right,in_successor.value)
            return root

    elif value > root.value:
        root.right = delete(root.right,value)
    else:
        root.left = delete(root.left,value)

    return root

inorder_traversal(rt)
print(" ")
delete(rt,2)
inorder_traversal(rt)