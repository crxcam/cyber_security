# modele.py
class TaskModel:
    def __init__(self):
        self.tasks = [str]

    def add_task(self, task: str):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks
