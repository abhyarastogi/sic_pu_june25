class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackSLL:
    def __init__(self):
        self.top = None  # Top of the stack (front of the SLL)

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # Insert at front
        self.top = new_node
        print(f"{data} pushed onto stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return
        removed = self.top.data
        self.top = self.top.next  # Remove from front
        print(f"{removed} popped from stack.")

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
        else:
            print(f"Top element is: {self.top.data}")

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            current = self.top
            print("Stack (top to bottom):", end=" ")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
if __name__ == "__main__":
    stack = StackSLL()

    while True:
        print("\n--- Stack Using SLL Menu ---")
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
