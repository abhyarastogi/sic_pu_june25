class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class StackDLL:
    def __init__(self):
        self.head = None
        self.tail = None  # Top of the stack (rear)

    def is_empty(self):
        return self.tail is None

    def push(self, data):
        new_node = Node(data)
        if self.tail is None:  # Stack is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print(f"{data} pushed onto stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return
        removed = self.tail.data
        if self.head == self.tail:  # Only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        print(f"{removed} popped from stack.")

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
        else:
            print(f"Top element is: {self.tail.data}")

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            current = self.head
            print("Stack (bottom to top):", end=" ")
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")
if __name__ == "__main__":
    stack = StackDLL()

    while True:
        print("\n--- Stack Using DLL (Rear) Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            value = input("Enter value to push: ")
            stack.push(value)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-5.")
