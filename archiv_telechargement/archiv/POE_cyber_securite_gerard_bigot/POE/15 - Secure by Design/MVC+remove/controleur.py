# controleur.py
from modele import TaskModel
from vue import display_task_list, get_new_task, show_main_menu, get_task_index


class TaskController:
    def __init__(self):
        self.model = TaskModel()

    def add_task(self):
        task = get_new_task()
        self.model.add_task(task)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        display_task_list(tasks)

    def remove_task(self):
        self.show_tasks()
        if self.model.get_tasks():  # Vérifie s'il y a des tâches à supprimer
            task_index = get_task_index()
            self.model.remove_task(task_index)
        else:
            print("Aucune tâche à supprimer.")

    def run(self):
        while True:
            choice = show_main_menu()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                break


if __name__ == "__main__":
    controller = TaskController()
    controller.run()
