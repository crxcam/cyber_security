Pour créer une application Python qui gère une liste chaînée, vous aurez besoin de définir une classe pour le nœud (Node) de la liste et une autre pour la liste chaînée elle-même. Ensuite, vous implémenterez les fonctions pour créer un nouveau nœud, supprimer un nœud, insérer un nœud et quitter l'application.

Voici un exemple simple de la manière dont vous pourriez structurer et implémenter une telle application :

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        
        if choice == '1':
            data = input("Enter data to insert: ")
            linked_list.insert_at_end(data)
        elif choice == '2':
            key = input("Enter data of the node to delete: ")
            linked_list.delete_node(key)
        elif choice == '3':
            prev_data = input("Enter the previous node data: ")
            data = input("Enter data to insert: ")
            linked_list.insert_after_node(prev_data, data)
        elif choice == '4':
            print("Current List: ")
            linked_list.print_list()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### Explication du code :
- **Node**: Une classe pour représenter chaque nœud de la liste chaînée.
- **LinkedList**: Une classe pour gérer la liste chaînée, incluant les méthodes pour insérer un nœud à la fin (`insert_at_end`), supprimer un nœud (`delete_node`), insérer un nœud après un autre (`insert_after_node`), et afficher la liste (`print_list`).
- **main**: Une boucle principale pour permettre à l'utilisateur de choisir des opérations sur la liste chaînée.

### Fonctionnement :
- L'utilisateur choisit parmi les opérations disponibles.
- Les données sont entrées par l'utilisateur pour chaque opération, et la liste chaînée est mise à jour ou affichée en conséquence.
- La boucle se termine lorsque l'utilisateur choisit de quitter (`5`).

Cet exemple de base peut être étendu ou modifié pour inclure d'autres fonctionnalités ou pour améliorer l'interaction utilisateur selon vos besoins.
