class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, element):
        new_node = StackNode(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

def are_parentheses_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []

    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token in precedence:
            while (not stack.is_empty() and stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)

expression1 = "(3 + 2) * (8 / 4)"
expression2 = "((3 + 2) * (8 / 4"
print(are_parentheses_balanced(expression1))  # True
print(are_parentheses_balanced(expression2))  # False

infix_expression = "3 + 5 * ( 2 - 8 )"
print(infix_to_postfix(infix_expression))  # 3 5 2 8 - * +
