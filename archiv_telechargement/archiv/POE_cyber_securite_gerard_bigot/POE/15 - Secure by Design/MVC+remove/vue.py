# vue.py
def display_task_list(tasks):
    print("Voici la liste de vos tâches :")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def get_new_task():
    return input("Entrez une nouvelle tâche : ")


def get_task_index():
    return int(input("Entrez le numéro de la tâche à supprimer : ")) - 1


def show_main_menu():
    print("1. Ajouter une tâche")
    print("2. Voir les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")
    return input("Que souhaitez-vous faire ? ")
