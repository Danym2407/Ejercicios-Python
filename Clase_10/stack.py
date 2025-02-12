# Last In First Out

class MyStack:
    def __init__(self):  # Constructor corregido
        self.n = 0
        self.a = []

    def push(self, x):
        self.a.append(x)
        self.n += 1

    def is_empty(self):
        return self.n == 0  # Forma más concisa

    def pop(self):
        if self.is_empty():
            print('The Stack is empty')
            return None
        self.n -= 1
        return self.a.pop()  # Corregido: usar self.a.pop()

    def count(self):
        return self.n


# Prueba del código
stack = MyStack()
stack.pop()  # Debería imprimir "The Stack is empty"
stack.push('D')
stack.push('A')
stack.push('N')
stack.push('Y')

print(stack.pop())  # Debería imprimir 'Y'
print(stack.pop())  # Debería imprimir 'N'
print(stack.pop())  # Debería imprimir 'A'
print(stack.pop())  # Debería imprimir 'D'

print(stack.count())  # Debería imprimir 0
print(stack.is_empty())
