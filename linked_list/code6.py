class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class linked_list:
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
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            #temp = self.head
            while (p != pos - 1 and temp.next!=None):
                temp = temp.next
                p += 1

            new_node.next = temp.next
            temp.next = new_node
            return

    def display(self):
        temp = self.head

        while temp.next:
            print(temp.data)
            temp = temp.next

        if temp:
            print(temp.data)


list = linked_list()

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

list.display()

list.insert(node(100), 600)

list.display()