from curses.ascii import isspace

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

Operators = set(['+', '-', '*', '/', '%', '(', ')', '^'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3} # dictionary having priorities of Operators

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
 
def infixToPostfix(expression): 

    #stack = [] # initialization of empty stack
    ops = Stack()

    output = '' 

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression
            output+= character;

        elif character=='(':  # else Operators push onto stack

            ops.push('(');

        elif character==')':

            while not ops.empty() and ops.top() != '(':
                output+=ops.top();
            ops.pop()
        else: 

            while not ops.empty() and ops.top() !='(' and Priority[character]<=Priority[ops.top()]:
                output+=ops.top();
            ops.push(character)
    while ops:
        output+=ops.top();

    return output

expression = input('Enter infix expression ')

#print('infix notation: ',expression)

print('postfix notation: ',infixToPostfix(expression))
