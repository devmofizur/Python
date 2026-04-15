class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        newNode = Node(data)
        if not self.head:  
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" > ")
            current = current.next
        print("None")

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def delete(self,data):
        if not self.head:
            print("Empty")
            return
        
        lastNode = self.head
        if(lastNode.data == data):
                self.head = lastNode.next
                return
        
        while lastNode.next:   
            if(lastNode.next.data == data):
                lastNode.next = lastNode.next.next
                return 
            lastNode = lastNode.next
        print("Not found")
        
Mylist = LinkedList()
Mylist.append(22)
Mylist.append(24)
Mylist.append(99)
Mylist.append('kibria')
Mylist.display()
Mylist.prepend('solaiman')
Mylist.display()
Mylist.append('monipur')
Mylist.display()
Mylist.prepend('Dhaka')
Mylist.prepend([2,3,4,5,6,7]])
Mylist.display()

Mylist.delete('x')
Mylist.display()

