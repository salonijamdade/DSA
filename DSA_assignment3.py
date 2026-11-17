
class node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None
class hospital_management:
    def __init__(self):
        self.front=self.rear= None

    # 1. Add Patient (enqueue)
    def enqueue(self, new_node):
        if self.front==None:
            self.front=self.rear=new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return

        temp=self.front
        while temp.next and temp.next.priority <= new_node.priority:
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        if new_node.next==None:
            self.rear=new_node

    # 2. Display the next patient to be treated. (display_next)
    def display_next(self):
        if self.front==None:
            print("Queue is empty")
            return

        temp=self.front
        print("Next patient to be treated:")
        print(temp.pid, temp.name, temp.priority)

    # 3.Remove a patient from the queue after treatment. (dequeue)
    def dequeue(self):
        if self.front==None:
            print("Queue is empty")
            return

        print("Treated patient:",
              self.front.pid,
              self.front.name,
              self.front.priority)

        self.front=self.front.next

        if self.front==None:
            self.rear=None

    # 4.Display all waiting patients in priority order(display_all)
    def display_all(self):
        if self.front==None:
            print("Queue is empty")
            return
        temp=self.front
        while temp:
            print("Patient ID:", temp.pid,
                  "Name:", temp.name,
                  "Priority:", temp.priority)
            temp=temp.next


# User defined input
pr = hospital_management()

n = int(input("Enter number of patients: "))

for i in range(n):
    pid=int(input("Enter patient ID: "))
    name=input("Enter patient name: ")
    priority=int(input("Enter priority (1-Critical, 2-Serious, 3-Normal): "))

    if priority not in [1, 2, 3]:
        print("Enter 1, 2 or 3.")
        continue
    pr.enqueue(node(pid, name, priority))


while True:
    print("\n1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        pid = int(input("Enter patient ID: "))
        name = input("Enter patient name: ")
        priority = int(input("Enter priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority in [1, 2, 3]:
            pr.enqueue(node(pid, name, priority))
        else:
            print("Invalid priority!")

    elif ch == 2:
        pr.display_next()

    elif ch == 3:
        pr.dequeue()

    elif ch == 4:
        pr.display_all()

    elif ch == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
