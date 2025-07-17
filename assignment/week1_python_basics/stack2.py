class Stack:

    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0

    def push(self):
        item = input('Enter item: ')
        self.stack.insert(0, item)
        print(f'{item} is pushed')

    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            print(self.stack[0])
            del self.stack[0]

    def peek(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            print(self.stack[0])

stack = Stack()
while True:
    print('1.Push\n2.Pop\n3.Peek\n4.Exit')
    choice = int(input('Enter your Choice: '))
    if choice == 4:
        break
    match(choice):
        case 1:
            stack.push()
        case 2:
            stack.pop()
        case 3:
            stack.peek()
        