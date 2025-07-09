class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return None if len(self.queue) < 1 else False
    
    def enqueue(self):
        item = input('Enter the element to add :')
        self.queue.insert(0, item)
        print(f'{item} was added successfully')

    def dequeue(self):
        if self.is_empty() == False:
            print(self.queue.pop())
        else:
            print('Queue is Empty')

    def display(self):
        if self.is_empty() == False:
            print(self.queue[::-1])
        else:
            print('Queue is Empty')

queue = Queue()
while True:
    print('1.Enqueue\n2.Dequeue\n3.Display\n4.Exit')
    choice = int(input('Enter your Choice: '))
    if choice == 4:
        break
    match(choice):
        case 1:
            queue.enqueue()
        case 2:
            queue.dequeue()
        case 3:
            queue.display()