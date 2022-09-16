
class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

rt = node(4)
l,r = node(2), node(5)
ll , lr = node(1) , node(3)
rr = node(8)
rrr = node(10)
rrl = node(7)


rt.left = l
rt.right = r
l.left = ll
l.right = lr
r.right = rr
rr.right = rrr
rr.left = rrl

def print_posible_path(root,arr=[]):
    if root is None: return

    if root.left is None and root.right is None:
        print(arr+[root.value])
        return

    print_posible_path(root.left,arr+[root.value])
    print_posible_path(root.right,arr+[root.value])


print_posible_path(rt)



