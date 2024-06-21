from dataclasses import dataclass


@dataclass
class Node:
    data: any
    next: "Node" = None  # Type hinting with a forward reference


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def insert_after_node(self, prev_node_data, data):
        cur_node = self.head
        while cur_node and cur_node.data != prev_node_data:
            cur_node = cur_node.next

        if not cur_node:
            print(f"Node with data {prev_node_data} not found.")
            return

        new_node = Node(data)
        new_node.next = cur_node.next
        cur_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")


def main():
    linked_list = LinkedList()

    while True:
        print("\nOperations on Linked List")
        print("1. Insert at End")
        print("2. Delete Node")
        print("3. Insert After Node")
        print("4. Display List")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter data to insert: ")
            linked_list.insert_at_end(data)
        elif choice == "2":
            key = input("Enter data of the node to delete: ")
            linked_list.delete_node(key)
        elif choice == "3":
            prev_data = input("Enter the previous node data: ")
            data = input("Enter data to insert: ")
            linked_list.insert_after_node(prev_data, data)
        elif choice == "4":
            print("Current List: ")
            linked_list.print_list()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
