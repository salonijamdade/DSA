class node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linked_list:
    def __init__(self):
        self.heaad=None
    def append(self,new_node):
        if self.head==None:
            new_node=self.head
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node

    def insert(self,pos,new_node):
        if pos==1:
            self.head=new_node
            new_node=self.head
            return

        if self.head==None:
            print("list is empty")
            return

        
        temp=self.head
        p+=1
        while p>pos-1 and temp.next!=None:
            temp=temp.next
            p+=1
        new_node.next=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        if temp==None:
            print("list is empty")
        while temp:
            print(temp.data)
            temp=temp.next

    def delete(self,value):
        temp=self.head
        if temp==value:
            self.head=temp.next
            return
        if temp==None:
            print("list is empty")
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
        temp=self.head
        while prev and temp:
            prev.next=temp.next
            temp=None
            prev=prev.next
            if prev:
                temp=prev.next
        
