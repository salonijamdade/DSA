
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
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next

            temp.next = new_node


    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        if self.head == None:
            print("List is empty")
            return

        temp = self.head
        p = 1

        while p < pos - 1 and temp.next != None:
            temp = temp.next
            p += 1

        new_node.next = temp.next
        temp.next = new_node


    def delete(self, value):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = temp.next
            return

        prev = temp
        temp = temp.next

        while temp != None:
            if temp.data == value:
                prev.next = temp.next
                return

            prev = temp
            temp = temp.next

        print("Value not found")


    def display(self):
        temp = self.head

        while temp != None:
            print(temp.data)
            temp = temp.next

  
    def reverse(self):
        prev = None
        temp = self.head

        while temp != None:
            new_node = temp.next
            temp.next = prev
            prev = temp
            temp = new_node

        self.head = prev

    def middle(self):
        slow=self.head
        fast=self.head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        if slow!=None:
            print("middle node",slow.data)

    def sum_consecutive(self):
        temp=self.head

        while temp!=None and temp.next!=None:
            total=temp.data+temp.next.data
            print(total)
            temp.next.data=total
            temp=temp.next
    


list = linkedlist()

n1 = node(1)
n2 = node(2)
n3 = node(3)

list.append(n1)
list.append(n2)
list.append(n3)

#print("Original list:")
#list.display()

list.insert(node(4), 2)
#print("After inserting 4 at position 2:")
#list.display()

#list.delete(2)
#print("After deleting 2:")
#list.display()

list.insert(node(6), 5)
list.insert(node(7), 6)
list.insert(node(7), 7)

list.display()

list.middle()

list.sum_consecutive()

#list.reverse()
#print("After reversing:")
#list.display()
