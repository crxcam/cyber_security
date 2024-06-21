# controleur.py
from modele import TaskModel
from vue import display_task_list, get_new_task, show_main_menu


class TaskController:
    def __init__(self):
        self.model = TaskModel()

    def add_task(self):
        task = get_new_task()
        self.model.add_task(task)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        display_task_list(tasks)

    def run(self):
        print(" *** entrée run")
        while True:
            choice = show_main_menu()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                print(" *** un tour pour rien")
                break
            else:
                print(" *** sortie run")


if __name__ == "__main__":
    controller = TaskController()
    controller.run()
