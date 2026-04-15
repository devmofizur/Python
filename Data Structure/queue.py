from collections import deque
import time

class Queue:
    def __init__(self):
        self.container = deque()
    def enqueue(self,val):
        self.container.append(val)
    def dequeue(self):
        self.container.popleft()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)


start = time.time()
Meow = Queue()

Meow.enqueue("kitty")
Meow.enqueue("royale")
Meow.enqueue("alpha cat")
Meow.enqueue("spoidermon")

print(Meow.is_empty())

print(Meow.container)
Meow.dequeue()
print(Meow.container)
end = time.time()

print ("Took", str((end-start)*1000),"milisec")