class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node

    def insert(self,new_node,pos):
        if pos==1:
            self.head=new_node
            return
        temp=self.head
        p=1
        while p<pos-1 and temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.next=temp

    def delete(self,value):
        temp=self.head
        if temp==None:
            print("list is empty")
        if temp==value:
            self.head=temp.next
        prev=temp
        temp=temp.next
        while temp:
            if temp.data==value:
                prev.next=temp.next
                temp=None
            prev=temp
            temp=temp.next

    def alt_del(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        prev=self.head
        temp=self.head.next
        while temp:
            prev.next=temp.next
            temp=None
            prev=prev.next
            if prev:
                temp=prev.next


    def display(self):
        if self.head==None:
            print("list is empty")
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

list=linked_list()
node1=node(1)
node2=node(2)
node3=node(3)
node4=node(4)
node5=node(5)

list.append(node1)
list.append(node2)
list.append(node3)
list.append(node4)
list.append(node5)

list.display()
list.alt_del()
list.display()
