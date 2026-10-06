class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(1)
node2=node(2)
node3=node(3)
node4=node(4)

node1.next=node2
node2.next=node3
node3.next=node4

key=2
temp=node1
while temp is not None:
    if temp.data==key:
        print("key found")
        break
    temp=temp.next
else:
    print("key not found")
