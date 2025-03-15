class StackNode:
    """Nodo individual de la pila."""
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """Implementación de una pila sin usar estructuras predefinidas como list o deque."""
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, element):
        """Agregar un elemento a la pila."""
        new_node = StackNode(element)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        """Eliminar y devolver el elemento superior de la pila."""
        if self.is_empty():
            raise IndexError("La pila está vacía")
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self):
        """Devolver el elemento superior sin eliminarlo."""
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        """Retornar True si la pila está vacía."""
        return self.top is None

    def size(self):
        """Retornar el número de elementos en la pila."""
        return self.count

# Validación de paréntesis balanceados
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

# Conversión de notación infija a postfija
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []

    tokens = expression.split()

    for token in tokens:
        if token.isalnum():  # Operandos
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

# Ejemplo de uso
expression1 = "(3 + 2) * (8 / 4)"
expression2 = "((3 + 2) * (8 / 4"
print(are_parentheses_balanced(expression1))  # True
print(are_parentheses_balanced(expression2))  # False

infix_expression = "3 + 5 * ( 2 - 8 )"
print(infix_to_postfix(infix_expression))  # 3 5 2 8 - * +
