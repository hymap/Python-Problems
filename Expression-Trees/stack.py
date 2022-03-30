""" Stack Adaptor Class using 'list' class 
Methods
  Create
  push 
  pop
  empty
  top
"""
class Stack:
    # Constructor to create empty Stack
    def __init__(self):
        self.ops = []

    # if length of Stack is 0 return true
    def empty(self):
        return len(self.ops) == 0

    # to look what is on the top
    def top(self):
        return self.ops[-1]

    # to pop from top of Stack
    def pop(self):
        return self.ops.pop()
    
    def push(self, value):
        self.ops.append(value)

    def popWhile(self, condition):
        post = ''
        while not self.empty() and condition(self.top()):
            post += self.top() + ' '
            self.pop()
        return post

    def size(self):
        return len(self.ops)
