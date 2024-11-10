# The Node class represents an individual element in the linked list
class Node:
  def __init__(self, data=None):
    self.data = data # To store the value of the node
    self.next = None # Next node in the list

#  LinkedList class handles the operations on the nodes in the list
class LinkedList:
  def __init__(self):
    self.head = None # The linked list is empty at first

  # Add a new node containing the given data to the end of the list
  def append(self, data):
    
    # Create a new node with the provided data
    new_node = Node(data)
    # If the list is empty, set the new node as the head of the list
    if self.head is None:
      self.head = new_node
      return
    
    # If the list isn't empty, move to the last node
    last_node = self.head
    while last_node.next:
      last_node = last_node.next

    # When the last node is reached, set its 'next' to the new node
    last_node.next = new_node

  # remove a node at a specific index.
  def remove_at(self, index):
    # Check if the index is invalid or the list is empty
    if index < 0 or self.head is None:
        return
    
    # If removing the first node, update the head
    if index == 0:
      self.head = self.head.next
      return
    
    # Find the node before the one to remove
    current_node = self.head 
    current_position = 0

    # Move to the node just before the target index
    while current_node.next and current_position < index - 1:
      current_node = current_node.next
      current_position += 1

    # If the next node exists, skip it by updating 'next'
    if current_node.next:
      current_node.next = current_node.next.next

  # Remove a node by its value  
  def remove_by_value(self, value):
    if self.head is None:
      return
  
    if self.head.data == value:
      self.head = self.head.next
      return
    
    current_node = self.head
    while current_node.next:
      if current_node.next.data == value:
        current_node.next = current_node.next.next
        return
      current_node = current_node.next
  
  # Add a node at a specific index
  def insert_by_index(self, index, data):
    if index < 0:
      return
    
    new_node = Node(data)
    if index == 0: 
      new_node.next = self.head
      self.head = new_node
      return

    current_node = self.head
    current_position = 0
    while current_node and current_position < index - 1:
      current_node = current_node.next
      current_position += 1
  
    if current_node:
      new_node = Node(data)
      new_node.next = current_node.next
      current_node.next = new_node

  # Method to print the elements of the linked list
  def display(self):
    # Start at the head and print each node's data
    current_node = self.head
    
    while current_node:
      print(current_node.data, end=' -> ')
      current_node = current_node.next # Move to the next node.

    print() # Print a newline

# Create a new LinkedList instance
linked_list = LinkedList()

# Append nodes to the list
linked_list.append(50)  # 0
linked_list.append(15)  # 1
linked_list.append(20)  # 2
linked_list.append(11)  # 3
linked_list.append(5)  # 4
linked_list.append(25)  # 5

# Remove nodes at specific indices and display after each removal
linked_list.display()
linked_list.remove_at(2)
linked_list.display()
linked_list.remove_at(2)
linked_list.display()
linked_list.remove_at(0)
linked_list.display()
linked_list.remove_at(2)
linked_list.display()

# Insert nodes at specific positions and show the list after inserting them
linked_list.insert_by_index(2, 13)
linked_list.insert_by_index(3, 14)
linked_list.insert_by_index(4, 17)
linked_list.display()

# Remove node by its value and display the list
linked_list.remove_by_value(15)
linked_list.display()