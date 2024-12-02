

class Task:
    """Класс, представляющий задачу."""

    def __init__(self, task_id: int, title: str, description: str, category: str, due_date: str, priority: str, status: str = "не выполнена"):
        """
        Инициализация задачи
        :param task_id: Уникальный идентификатор задачи
        :param title: Заголовок задачи
        :param description: Описание задачи
        :param category: Категория задачи (например, работа, личное, обучение)
        :param due_date: Срок выполнения задачи
        :param priority: Приоритет задачи (низкий, средний, высокий)
        :param status: Статус задачи (выполнена, не выполнена)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self) -> str:
        """ Возвращает строковое представление задачи. """
        return f"[ID: {self.id:<3}] | {self.title:<20} | {self.description:<20} | {self.category:<20} | {self.due_date:<20} | {self.priority:<20} | {self.status:<20}"

    def to_dict(self) -> dict:
        """Конвертирует объект задачи в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }


    @staticmethod
    def from_dict(data: dict) -> object:
        """
        Создает объект задачи из словаря
        :param data: словарь с данными для создания объекта
        :return: объект Task
        """
        return Task(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"],
            status=data["status"],
        )
