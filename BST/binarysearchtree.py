class node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root==None:
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<=temp.data: # left add if new_node is less than or equal to root
                    if temp.left==None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right==None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

def inorder(temp): #root is copied into the temp variable and then we check if temp is None or not. If it is None then we return else we print the left subtree, root and right subtree.
    if temp==None:
        return
    else:
        inorder(temp.left)
        print(temp.data,end=" ")
        inorder(temp.right)

btree=BST()
btree.insert(node(10))
btree.insert(node(20))
btree.insert(node(90))
btree.insert(node(40))
btree.insert(node(70))
btree.insert(node(55))
inorder(btree.root)


