# vue.py
def display_task_list(tasks):
    print("Voici la liste de vos tâches :")
    for task in tasks:
        print(f"- {task}")


def get_new_task():
    return input("Entrez une nouvelle tâche : ")


def show_main_menu():
    print("1. Ajouter une tâche")
    print("2. Voir les tâches")
    print("3. Quitter")
    return input("Que souhaitez-vous faire ? ")
