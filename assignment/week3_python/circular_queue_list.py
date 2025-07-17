class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Fixed size list
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"{data} enqueued.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:  # Only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"{removed} dequeued.")

    def peek(self):
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
        else:
            print(f"Front element is: {self.queue[self.front]}")

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
if __name__ == "__main__":
    size = int(input("Enter size of Circular Queue: "))
    cq = CircularQueue(size)

    while True:
        print("\n--- Circular Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            val = input("Enter value to enqueue: ")
            cq.enqueue(val)
        elif choice == '2':
            cq.dequeue()
        elif choice == '3':
            cq.peek()
        elif choice == '4':
            cq.display()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-5.")
