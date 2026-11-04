
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class Stack:
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
            return
        temp = self.top
        print("Popped element:", temp.data)
        self.top = self.top.next
        temp = None
    def display(self):
        if self.isempty():
            print("Stack is empty")
            return
        temp = self.top
        print("Stack elements:")
        while temp:
            print(temp.data)
            temp = temp.next
    def reverse_string(self, string):
        s = Stack()
        for i in string:
            s.push(Node(i))
        result = ""
        while not s.isempty():
            result += str(s.top.data)
            s.pop_silent()

        print("Reversed string:", result)
    def pop_silent(self):
        if self.isempty():
            return None

        temp = self.top
        value = temp.data
        self.top = self.top.next
        temp = None
        return value

    def reverse_stack(self):
        s2 = Stack()

        temp = self.top
        while temp:
            s2.push(Node(temp.data))
            temp = temp.next

        self.top = s2.top
        print("Stack reversed successfully")


st = Stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))

st.display()

st.pop()
st.display()

st.reverse_string("Saloni")

st.reverse_stack()
st.display()
