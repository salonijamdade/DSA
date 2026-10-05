class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(10)
node2=node(20)
node3=node(30)
node1.next=node2
node2.next=node3

new=node(50)
new.next=node1
node1=new


while node1 is not None:
    print(node1.data)
    node1=node1.next