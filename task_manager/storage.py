import json
from .task import Task


class StorageError(Exception):
    """Исключения для работы с хранилищем"""


class Storage:
    """ Класс для работы с хранилищем данных."""

    def __init__(self, filename: str = "tasks.json") -> None:
        self.filename = filename

    def save(self, task_manager: object) -> None:
        """Сохраняет список задач в файл."""
        try:
            data = {
                "tasks": [task.to_dict() for task in task_manager.tasks],
                "current_id": task_manager.current_id,
            }
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception:
            raise StorageError("Ошибка при сохранении данных.")

    def load(self, task_manager: object) -> None:
        """ Загружает данные из файла в список задач."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                task_manager.tasks = [Task.from_dict(task) for task in data["tasks"]]
                task_manager.current_id = data["current_id"]
        except FileNotFoundError:
            print("Файл не найден. Начинаем с пустой библиотеки.")
        except json.JSONDecodeError:
            raise StorageError("Ошибка декодирования файла данных.")
        except Exception:
            raise StorageError("Ошибка при загрузке данных.")
