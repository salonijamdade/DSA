class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        if self.head==None:
            self.node=new_node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node

    def insert(self,new_node,pos):
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return

        if self.head==0:
            print("list is empty")
            return

        temp=self.head
        p=1

        while p<pos-1 and temp.next!=None:
            temp=temp.next
            p+=1

        new_node.next=temp.next
        temp.next=new_node


    def delete(self,value):
        temp=self.head

        if temp==None:
            print("list is empty")
            return

        if temp.data==value:
            self.head=temp.next 
            return

        prev=temp
        temp=temp.next

        while temp!=None:
            if temp.data==value:
                prev.next=temp.next
                return
            prev=temp
            temp=temp.next

        print("value not found")

    def display(self):
        temp=self.head

        while temp!=None:
            print(temp.data)
            temp=temp.next 


list=linkedlist()

n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)


list.display()

        

            

    