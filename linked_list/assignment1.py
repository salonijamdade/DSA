class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node

    def insert (self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head=new_node
        else:
            p=1
            while(p!=pos-1 and temp.next!=None):
                temp=temp.next
                p+=1

            new_node.next=temp.next
            temp.next=new_node
            return

    def delete(self,value):
        temp=self.head
        prev=None
        if temp.data==value:
            self.head=self.head.next
            return
        while(temp):
            if(temp.data==value):
                break
            else:
                prev=temp
                temp=temp.next
        if temp==None:
            print("value is not present")
            return
        prev.next=temp.next
        temp=None

    def display(self):
        temp=self.head

        while temp.next!=None:
            print(temp.data)
            temp=temp.next
        if temp:
            print(temp.data)

list=linkedlist()
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)



list.display()

list.delete(2)
list.display()



             
