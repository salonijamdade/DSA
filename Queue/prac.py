class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class lq:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear==None:
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    def dequeue(self):
        if self.front==None:
            print("queue is empty")
            return
        temp=self.front
        self.front=self.front.next
        if self.front==None:
            self.rear=None

        temp=None

    def display(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next

q=lq()
q.enqueue(node(1))
q.enqueue(node(2))
q.enqueue(node(3))
q.enqueue(node(4))
q.enqueue(node(5))
q.display()
