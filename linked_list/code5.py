class node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if(self.head==None):
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node

    def display(self):
        temp=self.head
        while temp.next:
            print(temp.data)
            temp=temp.next.next
        if temp:
            print(temp.data)

list=LinkedList()
n1=node(10)
n2=node(-20)
n3=node(30)
n4=node(-40)
n5=node(50)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(n5)
list.display()

