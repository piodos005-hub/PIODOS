
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_from_head(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def display(self):
        current = self.head
        if not current:
            return "EMPTY"
        result = ""
        while current:
            result += f"{current.data} -> "
            current = current.next
        result += "NULL"
        return result

print("=== 2. INTERACTIVE LINKED LIST PROGRAM ===")
ll = LinkedList()
print("Created an empty linked list.")

print("\n--- MANUAL INSERTION AT TAIL ---")
print("Type letters one by one. Type 'done' when you are finished.")
while True:
    val = input("Enter letter to insert: ").strip()
    if val.lower() == 'done':
        break
    if val:
        ll.insert_at_tail(val)
        print(f"Current Linked List: {ll.display()}")

print(f"\nFinal Linked List before deletion: {ll.display()}")

print("\n--- MANUAL DELETION FROM HEAD ---")
while ll.head is not None:
    input(f"Current list: {ll.display()}. Press Enter to delete from head: ")
    removed = ll.delete_from_head()
    print(f"Deleted: {removed}")

print(f"\nFinal Linked List after deletion: {ll.display()}")
print("STOP")