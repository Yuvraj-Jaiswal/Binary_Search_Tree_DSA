from LevelOrderTraversal import breath_first_search

class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value


def insert(root,val):
    if root is None:
        return node(val)

    if val > root.value:
        root.right = insert(root.right , val)
    else:
        root.left = insert(root.left , val)

    return root

num = [5,1,3,4,2,7]
root = None
for i in num:
    root = insert(root,i)

breath_first_search(root)






