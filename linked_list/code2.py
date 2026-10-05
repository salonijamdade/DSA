class node:
    def __init__(self,data):
        self.data=data
        self.next=None


node1=node(1)
node2=node(2)
node3=node(3)
node4=node(4)
node5=node(5)
node6=node(6)

while node1 is not None:
    print(node1.data)
    node1=node1.next


count=0 

temp=node1

while temp is not None:
    count+=1
    temp=temp.next

print(count)






