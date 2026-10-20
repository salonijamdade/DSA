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
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        p=1
        while p<pos-1 and temp.next:
            temp=temp.next
            p+=1
        new_node.next=temp.next
        temp.next=new_node

    def delete(self,value):
        temp=self.head
        if temp==None:
            print("list is empty")
            return
        
        if temp==value:
            self.head=temp.next
            return
        prev=temp
        temp=temp.next
        while temp:
            if temp.data==value:
                prev.next=temp.next
                return
            prev=temp
            temp=temp.next
    def del_alt(self):
        prev=self.head
        temp=self.head.next
        while prev and temp:
            prev.next=temp.next
            temp=None
            prev=prev.next
            if prev:
                temp=prev.next
        

    def display(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        while temp:
            print(temp.data)
            temp=temp.next


list=linked_list()
n1=node(1)
n2=node(2)
n3=node(3)
n4=node(4)
n5=node(5)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(n5)
list.display()
#list.delete(2)
#list.display()
list.del_alt()
list.display()
