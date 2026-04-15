# stack = []
# stack.append("meow")
# stack.append("cat")
# stack.append("sit")
# stack.append(152)
# stack.append(22.11)
# print(stack)

# print(stack[-1])


# ======> Stack is bad practice because it is dynamic array <======
# ======> It allocates more memory space than actual size and also copies all element to new memory location if contiguous memory space is filled to new memory location <=====

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

newStack = Stack()
print(newStack.size())
newStack.push(5)
print(newStack.size())
newStack.push("lazy")
print(newStack.size())
newStack.push(15.66)
newStack.push("alpha")

print(newStack.container)
