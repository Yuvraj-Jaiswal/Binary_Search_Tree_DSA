
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

def search_bst(root,k):
    if root is None : return False
    if root.value == k : return True

    if k > root.value:
        find = search_bst(root.right,k)
    else:
        find = search_bst(root.left,k)

    if find: return True
    else: return False

print(search_bst(rt,3))
