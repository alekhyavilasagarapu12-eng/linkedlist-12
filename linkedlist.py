class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
          self.head = new_node
          return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node
    def add_beg(self, data):
        obj = Node(data)
        if self.head is None:
            self.head = obj
            return
        obj.next=self.head
        self.head = obj
        
        
    def display(self):
        itr = self.head
        while itr:
            print(itr.data, end=" -> ")
            itr = itr.next
ll = LinkedList()
ll.add_end(50)
ll.add_end(60)
ll.add_end(70)
ll.add_end(80)
ll.add_end(90)
ll.add_beg(40)
ll.display()




   