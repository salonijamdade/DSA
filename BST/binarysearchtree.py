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

    def inorder(self,temp): #root is copied into the temp variable and then we check if temp is None or not. If it is None then we return else we print the left subtree, root and right subtree.
        if temp==None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)
    def postorder(self,temp):
        if temp==None:
            return
        else:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data,end=" ")
    def preorder(self,temp):
        if temp==None:
            return
        else:
            print(temp.data,end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)
    def search(self,value):
        temp=self.root
        while temp!=None:
            if value==temp.data:
                print("element found")
                return
            elif value<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        print("element not found")

    def min(self):
        temp=self.root
        if temp==None:
            print("tree is empty")
            return
        while temp.left!=None:
            temp=temp.left
        print(temp.data)
    def max(self):
        temp=self.root
        if temp==None:
            print("tree is empty")
            return
        while temp.right!=None:
            temp=temp.right
        print(temp.data)


    def delete(self,rt,value):
        if rt is None:
            return None

        if value<rt.data:
            rt.left=self.delete(rt.left,value)

        elif value>rt.data:
            rt.right=self.delete(rt.right,value)

        else:
            if rt.left is None:
                return rt.right

            elif rt.right is None:
                return rt.left

            succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right=self.delete(rt.right,succ.data)

        return rt

    def get_successor(self,temp):
        temp=temp.right
        while temp.left!=None:
            temp=temp.left
        return temp   
    # def search(self,value):
    #     temp=self.root
    #     while temp:
    #         if value.data==temp:
    #             # print("element found")
    #             return True
    #         elif value<temp.data:
    #             temp=temp.left
    #         else:
    #             temp=temp.right
    #     # print("element not found")
    #     return False



btree=BST()
btree.insert(node(10))
btree.insert(node(20))
btree.insert(node(90))
btree.insert(node(40))
btree.insert(node(70))
btree.insert(node(55))
btree.inorder(btree.root)
# btree.root=btree.delete(btree.root,40)
# print("after deleteing")
# btree.inorder(btree.root)
# btree.min()
btree.search(90)




