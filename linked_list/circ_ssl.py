class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

  
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            new_node.next=self.head
        else:
            temp = self.head

            while temp.next!=self.head:
                temp=temp.next

            temp.next=new_node
            new_node.next=self.head


    def insert(self, new_node, pos):
        if pos==1:
            temp=self.head
            while(temp.next!=self.head):# traverse to last node to find address of last node and join it to the first node 
                temp=temp.next 
            new_node.next=self.head#if while loop false assign new node to the address to the last node
            self.head=new_node#make it self head 
            temp.next=self.head#circular link made
        else:
            p=1             #for inserting new node to the 2nd last or last position.
            temp=self.head
            while(p != pos - 1):
                temp=temp.next 
            new_node.next=temp.next 
            temp.next=new_node



    def delete(self, value):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:
            while temp.next!=self.head:
                temp=temp.next 
            self.head = temp.next
            temp.next=self.head 
        else:
            while(temp.data!=value and temp):
                prev=tempemp=temp.next
                temp=temp.next
                if temp==self.head:
                    print("value is not present in the list")
                    return
            prev.next=temp.next 
            temp=None

    def display(self):
        temp = self.head

        while True:
            print(temp.data)
            temp = temp.next
            if temp==self.head:
                break

list = linkedlist()

n1 = node(10)
n2 = node(20)
n3 = node(30)
n4 = node(40)
n5 = node(50)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(n5)



#list.insert(node(6),6)
#list.insert(node(33),3)
list.delete(50)

list.display()