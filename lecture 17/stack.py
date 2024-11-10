# The Node class represents an individual element in the linked list
class Node:
  def __init__(self, data=None):
    self.data = data # To store the value of the node
    self.next = None # Next node in the list

# Define the Stack class to manage stack operations
class Stack:
  def __init__(self):
    # Start with an empty stack and length 0
    self.top_node = None
    self.length = 0

# Check if the stack is empty
  def empty(self):
    return self.length == 0
  
  # Get the current size of the stack
  def size(self):
    return self.length

  # Add a new node to the top of the stack
  def push(self, data):
    new_node = Node(data) # Create a new node
    new_node.next = self.top_node # Link the new node to the top
    self.top_node = new_node # Update the top node
    self.length += 1 # Increment the stack size

  # Remove and return the top item from the stack
  def pop(self):
    if not self.empty():
      popped_item = self.top_node.data  # Get the data from the top
      self.top_node = self.top_node.next # Move the top to the next node
      self.length -= 1 # Decrease the stack size
      return popped_item
    else:
      raise IndexError("Stack is empty") # Raise an error if the stack is empty


# Create a new Stack instance
stack = Stack()

print(stack.empty())
print(stack.length)

# Push elements onto the stack
stack.push(200)
stack.push(50)
stack.push(75)
stack.push(25)
stack.push(30)

print(stack.empty())
print(stack.length)

# Pop elements and check stack state after each operation
print(stack.pop())
print(stack.empty())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.length)
print(stack.pop())
print(stack.empty())
print(stack.length)
print(stack.pop())