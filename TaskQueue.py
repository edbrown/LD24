from definitions import *
from collections import deque

class Task():

    def __init__(self, data, task_type):
        self.task_type = task_type
        self.data = data

    def is_walk(self):
        return self.task_type == TASK_WALK

    def is_attack(self):
        return self.task_type == TASK_ATTACK

    def is_action(self):
        return self.task_type == TASK_ACTION

    def is_speak(self):
        return self.task_type == TASK_SPEAK
        

class TaskQueue():

    def __init__(self):
        self.tasks = deque()

    def get_task(self):
        item = self.tasks.popleft()
        self.tasks.appendleft(item)
        return item

    def remove_task(self):
        return self.tasks.popleft()

    def add_task(self, data, task_type = TASK_HALT):
        return self.tasks.append(Task(data, task_type))

    def has_tasks(self):
        return len(self.tasks) != 0

    def clear_tasks(self):
        self.tasks = deque()
