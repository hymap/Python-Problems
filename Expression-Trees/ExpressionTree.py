# Evaluate Postfix Expression
from logging import exception
import stack
class Node:
    def __init__(self, op, left=None, right=None):
        # Contain a part of the expression
        self.op = op
        self.left = left
        self.right = right
    '''Methods:
    node_eval(self)
      if self.op is Operator
        left = node_eval(self.left)
        right = node_eval(self.right)
      else
        return self.op
      end

      return (left op right)
      '''    
    def eval(self):
        opers = {
            '+': lambda l,r: l+r,
            '-': lambda l,r: l-r,
            '*': lambda l,r: l*r,
            '/': lambda l,r: l/r,
            '%': lambda l,r: l%r,
            '^': lambda l,r: l**r
        }
        if self.isLeaf():
            return self.op
        else:
            v_left = self.left.eval()
            v_right = self.right.eval()
            return opers[self.op](int(v_left), int(v_right))

    def isLeaf(self):
        # return true is 
        # self.left is None
        # self.right is None
        return (self.left==None) and (self.right==None)   

    def printNode(self):
        
        if self.isLeaf():
            #print(self.op, end='')
            return self.op
        else:
            v_left = self.left.printNode()
            v_right = self.right.printNode()
            expr = self.op + '(' + v_left + ',' + v_right + ')'
            return expr

class ExpressionTree:
    def __init__(self, expression):
        operators = '+-*/%^'
        stuff = expression.split()
        # To check what is in stuff you can uncomment the below line
        # print(stuff)
        nodes = stack.Stack()
        for op in stuff:
            if op in operators:
                # pop things off the stack. Since we use binary operators
                # we need atleast two operands on the stack. 
                if nodes.size() < 2:
                    raise Exception("Insufficient Operands")
                right = nodes.top()
                nodes.pop()
                left = nodes.top()
                nodes.pop()
                # Create new node of sub-tree and Push into Stack
                nodes.push(Node(op,left,right))
            else:
                nodes.push(Node(op))

        # now what ?
        if nodes.size() == 1:
            self.root = nodes.top()
        else:
            # we decide
            pass

    def eval(self):
        return self.root.eval()

    def prnTree(self):
        return self.root.printNode()


# Read line by line and 
# Store each line in a list object
# Process each line until end of list 
# End
PostfixLines = []
# Start reading a i/p line
exp=input()
while True:
    # if not blank line
    if exp:
        # append i/p line to infixLines list
        PostfixLines.append(exp)
        # read next i/p line and loop
        exp=input()
    else:
        # if blank line then break from while loop
        break

# for each infix line print the postfix expression
for exp in PostfixLines:
  myTree = ExpressionTree(exp)
  print("The Expression tree is ", myTree.prnTree())
  print("The value is ", myTree.eval())
