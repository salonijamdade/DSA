
class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear == None:  # Queue is empty
            self.front = self.rear = new_node
        else:                  # Queue is not empty
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
            return

        temp = self.front
        print("Deleted:", temp.data)
        self.front = self.front.next

        if self.front ==None:
            print("queue is empty now")
            self.rear = None

        temp = None

    def display(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next


queue = LQueue()

queue.enqueue(node(1))
queue.enqueue(node(2))
queue.enqueue(node(3))
queue.enqueue(node(4))
queue.enqueue(node(5))

queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()