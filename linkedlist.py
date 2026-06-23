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
    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    def remove_beg(self,data):
        if self.head is None:
            return
        self.head=self.head.next
    def remove_end(self,data):
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None
    def add_pos(self, pos, data):
        if pos == 0:
            self.add_beg(data)
            return
        itr = self.head
        for i in range(pos - 1):
            itr = itr.next
        new_node = Node(data)
        new_node.next = itr.next
        itr.next = new_node
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    def duplicate(self):
        if self.head is None:
            return
        seen = set()
        itr = self.head
        prev = None
        while itr:
            if itr.data in seen:
                prev.next = itr.next
            else:
                seen.add(itr.data)
                prev = itr
            itr = itr.next
        return self.head
    def remove_any_two(self, data):
        if self.head is None:
            return
        count = 0
        itr = self.head
        prev = None
        while itr:
            if itr.data == data:
                count += 1
                if count <= 2:
                    if prev is None:
                        self.head = itr.next
                    else:
                        prev.next = itr.next
            else:
                prev = itr
            itr = itr.next
    
        
        
    

        
        
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
ll.middle()
ll.remove_beg(40)
ll.remove_end(90)
ll.display()
l1=LinkedList()
l1.duplicate()
l1.remove_any_two(60)
l1.display()




