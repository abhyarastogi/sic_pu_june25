class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueSLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} enqueued successfully.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"{removed} dequeued successfully.")

    def peek(self):
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
        else:
            print(f"Front element is: {self.front.data}")

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            current = self.front
            print("Queue elements:", end=" ")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
if __name__ == "__main__":
    queue = QueueSLL()

    while True:
        print("\n--- Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            value = input("Enter value to enqueue: ")
            queue.enqueue(value)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            queue.display()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-5.")
