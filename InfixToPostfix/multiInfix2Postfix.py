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

def infix2Postfix(exp):
    ops = Stack()
    # Create a dictionary having priorities for Operators
    Priority = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3, '(':4 } 
    operators = '()+-*/%^'
    post=""
    openBracket=0
    closedBracket=0
    for c in exp:
        if isspace(c): continue
        if not c in operators:
            post += c
            continue
        # Have an operator
        # Place a space behind the last operand
        post += ' '
        if c == '(':
            ops.push(c)
            openBracket += 1
        elif c == ')':
            closedBracket += 1
            while not ops.empty() and ops.top() != '(':
                post += ops.top()
                # Place a space behind the operator
                post += ' '
                # pop off the top that is written to the 'post' variable              
                ops.pop()

            if ops.empty():
                raise Exception('missmatched...paranthesis..missing "("')
            # rp pop the paranthesis out and does not 
            # have to go into post fix expression
            ops.pop()
        elif c == '^':
            ops.push(c)
        else:
            # We skip populating the opening '(' into the post fix expression
            while not ops.empty() and ops.top() != '(' and Priority[c] <= Priority[ops.top()]:
                post += ops.top()
                # Place a space behind the operator
                post += ' '
                ops.pop()
            ops.push(c)
    # empty the Stack
    # Here you can check if there is an opening '(' without a closing ')' 
    # If so raise an exception
    while not ops.empty():
        # Place a space before the operator
        post += ' '
        post += ops.top()
        ops.pop()
    if openBracket != closedBracket:
        raise Exception('missmatched...paranthesis')

    return post

# Read line by line and 
# Store each line in a list object
# Process each line until end of list 
# End
infixLines = []
# Start reading a i/p line
exp=input()
while True:
    # if not blank line
    if exp:
        # append i/p line to infixLines list
        infixLines.append(exp)
        # read next i/p line and loop
        exp=input()
    else:
        # if blank line then break from while loop
        break

# for each infix line print the postfix expression
for exp in infixLines:
    print(infix2Postfix(exp))
