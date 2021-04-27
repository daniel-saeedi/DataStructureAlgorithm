class Stack:
     def __init__(self):
        self.items = []

     def isEmpty(self):
        return self.items == []

     def push(self, item):
        self.items.append(item)

     def pop(self):
        return self.items.pop()

     def peek(self):
        return self.items[self.size()-1]

     def size(self):
        return len(self.items)

class Converter:
    def __init__(self):
        self.stack = Stack()
        self.operators_precedence = {
            '^' : 3,
            '*' : 2,
            '/' : 2,
            '+' : 1,
            '-' : 1
        }
        self.ops = ['+', '-', '*', '/', '(', ')']

    def hasLessOrEqualPriority(self, a, b):
        if a not in self.operators_precedence:
            return False
        if b not in self.operators_precedence:
            return False
        return self.operators_precedence[a] <= self.operators_precedence[b]

    def isOperator(self, x):
        return x in self.ops

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def infixToPrefix(self,expression):
        op_stack = []
        exp_stack = []
        for ch in expression:
            if not ch in self.ops:
                exp_stack.append(ch)
            elif ch == '(':
                op_stack.append(ch)
            elif ch == ')':
                while op_stack[-1] != '(':
                    op = op_stack.pop()
                    a = exp_stack.pop()
                    b = exp_stack.pop()
                    exp_stack.append( op+b+a )
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and self.operators_precedence[ch] <= self.operators_precedence[op_stack[-1]]:
                    op = op_stack.pop()
                    a = exp_stack.pop()
                    b = exp_stack.pop()
                    exp_stack.append( op+b+a )
                op_stack.append(ch)
        
        while op_stack:
            op = op_stack.pop()
            a = exp_stack.pop()
            b = exp_stack.pop()
            exp_stack.append( op+b+a )
        return exp_stack[-1]

    
    #Reverses an infix expression and replace ( with ) and vice versa
    def reverseExp(self,expression) :
        expression = expression[::-1]
        reversed = str()
        for i in range(0,len(expression)) :
            if (expression[i] == '(') :
                reversed += ')'
                i += 1
            elif expression[i] == ')' :
                reversed += '('
                i += 1
            else :
                reversed += expression[i]
        
        return reversed

    """ 
    Algorithm :
        Read the Prefix expression in reverse order (from right to left)
        If the symbol is an operand, then push it onto the Stack
        If the symbol is an operator, then pop two operands from the Stack 
        Create a string by concatenating the two operands and the operator after them. 
        string = operand1 + operand2 + operator 
        And push the resultant string back to Stack
        Repeat the above steps until end of Prefix expression.
    """
    def prefixToPostfix(self,expression) :
        expression = expression[::-1]
        for token in expression :
            if self.isOperand(token) :
                self.stack.push(token)
            elif self.isOperator(token) :
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                self.stack.push(operand1+operand2+token)
        
        return self.stack.pop()

def cin() :
    string = input().strip()
    while string == "" :
        string = input().strip()
    return string

def main() :
    ops = ['+', '-', '/', '*','^']
    expression = cin()
    expression = expression.replace(" ", "")
    conv = Converter()
    if expression[0] in ops :
        print(conv.prefixToPostfix(expression))
    else :
        print(conv.infixToPrefix(expression))

main()