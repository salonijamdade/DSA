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
        count=0
        sum=0
        temp=self.head
        while temp is not None:
            count=count+1
            if temp.data%2==0:
                print(temp.data)
            sum=sum+temp.data
            temp=temp.next
        print(count)
        print(sum)

list=LinkedList()
n1=node(10)
n2=node(20)
n3=node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(node(40))
list.display()

