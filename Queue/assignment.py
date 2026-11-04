
# Linear Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return self.front is None

    # Q1Enqueue
    def enqueue(self, new_node):
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Q2. Dequeue
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return

        temp = self.front
        print("Deleted:", temp.data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        temp = None

    # Q3. Display
    def display(self):
        if self.isempty():
            print("Queue is empty")
            return

        temp = self.front
        print("Queue elements:")

        while temp:
            print(temp.data)
            temp = temp.next

    # Q4.Reverse Queue using Stack
    def reverse_queue(self):
        stack = []

        temp = self.front

        while temp:
            stack.append(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while stack:
            self.enqueue(Node(stack.pop()))

        print("Queue reversed successfully")

    # Q5. Merge Two Queues
    def merge(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(Node(temp.data))
            temp = temp.next

        print("Queues merged successfully")

    # Q6. Check if Two Queues are Identical
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                print("Queues are not identical")
                return

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            print("Queues are identical")
        else:
            print("Queues are not identical")

q1 = LQueue()
q2 = LQueue()

q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(30))

q2.enqueue(Node(10))
q2.enqueue(Node(20))
q2.enqueue(Node(30))

print("First Queue:")
q1.display()

print("Second Queue:")
q2.display()

q1.dequeue()
q1.reverse_queue()
q1.display()
q1.merge(q2)
q1.display()

q1.identical(q2)
