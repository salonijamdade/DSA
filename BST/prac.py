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
                if new_node.data<temp.data:
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

    def inorder(self,temp):
        if temp ==None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)
    def postorder(self,temp):
        if temp ==None:
            return
        else:
            self.inorder(temp.left)
            
            self.inorder(temp.right)
            print(temp.data,end=" ")
    def preorder(self,temp):
        if temp ==None:
            return
        else:
            
            print(temp.data,end=" ")
            self.inorder(temp.left)
            self.inorder(temp.right)
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

    def minmax(self):
        temp=self.root
        while temp.left!=None:
            temp=temp.left
        print("minimum",temp.data)

        temp=self.root
        while temp.right!=None:
            temp=temp.right
        print("maximum",temp.data)

        def get_successor(self,temp):
        temp=temp.right
        while temp.left!=None:
            temp=temp.left
        return temp   
    
    def level_order(self,rt):
        if rt is None:
            print("bst is emoty")
            return
        arr=[]
        count=0 #for counting the visited nodes
        level=0
        arr.append(rt)
        while count<len(arr):
            nodes=len(arr)-count
            print("\nlevel",level,end=" ")
            for i in range(nodes):
                temp=arr[count] #add the nodes to the array,takes the temp value according to the count value
                count+=1 #increase the counter of the visted nodes
                print(temp.data,end=" ")
                if temp.left:
                    arr.append(temp.left) # add the left node of the root
                if temp.right:
                    arr.append(temp.right) #add the right node of the root
            level+=1

        print("height of the tree",level)
        



bt=BST()
bt.insert(node(10))
bt.insert(node(50))
bt.insert(node(30))
bt.insert(node(80))
bt.insert(node(20))
bt.inorder(bt.root)
print()
bt.postorder(bt.root)
print()
bt.preorder(bt.root)
print()
bt.search(20)
print()
bt.minmax()
bt.level_order(bt.root)

                