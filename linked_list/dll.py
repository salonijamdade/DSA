
class node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def insert(self, new_node, pos):
        temp = self.head

        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
        else:
            p=1

            while p < pos - 1 and temp.next:
                temp = temp.next
                p += 1

            new_node.next = temp.next

            if temp.next:
                temp.next.prev = new_node

            temp.next = new_node
            new_node.prev = temp

    def reverse(self):
        temp = self.head
        print("List elements:")

        while temp != None:    #traversing to the end of the list
            #print(temp.data, end=" ")
            temp = temp.next 
        while temp:             #for printing the prev pointer
            print(temp.data, end=" ")
            temp=temp.prev

    def delete(self,value):
            temp=self.head
            prev=None
            #deleting first node
            if temp.data==value:
                self.head=self.head.next
                self.head.prev=None
                return
            while (temp):            #searching value
                if temp.data==value:
                    break
                else:                #traverse
                    prev=temp
                    temp=temp.next
    
            if temp==None:
                print("value is not in the list")
                return
            prev.next=temp.next
            temp=None

    def display(self):
        temp = self.head
        print("List elements:")

        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next


my_list = linkedlist()

n1 = node(1)
n2 = node(11)
n3 = node(111)
n4 = node(1111)
n5 = node(11111)

my_list.append(n1)
my_list.append(n2)
my_list.append(n3)
my_list.append(n4)
my_list.append(n5)

my_list.insert(node(111111), 6666)

my_list.display()

my_list.reverse()

