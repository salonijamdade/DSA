
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None

        temp = self.top
        popped_value = temp.data
        self.top = self.top.next
        temp = None
        return popped_value

    def display(self):
        temp = self.top
        print("Stack elements:")
        while temp:
            print(temp.data)
            temp = temp.next


class Lqueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isempty(self):
        return self.front is None

    def enqueue(self, new_node):
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        temp = self.front
        deleted_value = temp.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        temp = None
        return deleted_value

    def display(self):
        temp = self.front
        print("Queue elements:")
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


def reverse_stack(s1):
    q1 = Lqueue()

    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))

    # q1.display()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.display()


def reverse_queue(q1):
    s1 = stack()

    while q1.front is not None:
        s1.push(Node(q1.dequeue()))

    while not s1.isempty():
        print(s1.pop())



que = Lqueue()
st = stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))

st.display()
reverse_stack(st)
