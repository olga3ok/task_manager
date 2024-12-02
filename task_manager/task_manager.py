from .task import Task


class TaskManagerError(Exception):
    """Базовое исключение для TaskManager"""


class TaskNotFoundError(TaskManagerError):
    """Исключение, возникающее при отсутствии задачи"""


class TaskManager:
    """Класс для управления списком задач"""
    def __init__(self) -> None:
        self.tasks = []
        self.current_id = 1

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str) -> object:
        """
        Добавляет новую задачу
        :param title: Заголовок задачи
        :param description: Описание задачи
        :param category: Категория задачи (например, работа, личное, обучение)
        :param due_date: Срок выполнения задачи
        :param priority: Приоритет задачи (низкий, средний, высокий)
        :return: Объект новой задачи
        """
        task = Task(self.current_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.current_id += 1
        return task

    def complete_task(self, task_id: int) -> object:
        """Отмечает задачу как выполненную"""
        for task in self.tasks:
            if task_id == task.id:
                task.status = "выполнена"
                return task
        raise TaskNotFoundError(f"Задача с ID {task_id} не найдена.")

    def delete_task(self, task_id: int) -> None:
        """Удаляет задачу по идентификатору"""
        initial_lenth = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) == initial_lenth:
            raise TaskNotFoundError(f"Задача с ID {task_id} не найдена.")

    def search_tasks(self, keyword: str) -> list:
        """Поиск задачи по ключевому слову"""
        return [task for task in self.tasks
                if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower() or keyword.lower() in task.category.lower() or keyword.lower() in task.status.lower()
                ]

    def display_tasks(self) -> list:
        """Возвращает список всех задач"""
        return self.tasks

    def edit_task(self, task_id: int, field: str, value):
        """
        Изменяет значение указанного поля задачи.
        :param task_id: ID задачи, которую нужно отредактировать
        :param field: Название поля для изменения
        :param value: Новое значение для указанного поля
        :return: Обновленная задача
        """
        for task in self.tasks:
            if task.id == task_id:
                setattr(task, field, value)
                print(f"Значение поля {field} изменено на {value}")
                return task
        print(f"Задача с ID {task_id} не найдена.")





