from datetime import datetime
from .task_manager import TaskManager, TaskNotFoundError
from .storage import Storage


class Menu:
    """Класс для управления меню приложения"""
    def __init__(self):
        self.manager = TaskManager()
        self.storage = Storage()
        self.load_data()

        # Словарь для вызова методов по выбору пользователя
        self.choices = {
            "1": self.display_tasks,
            "2": self.add_task,
            "3": self.edit_task,
            "4": self.complete_task,
            "5": self.search_tasks,
            "6": self.delete_task,
            "0": self.exit_program,
        }

    def load_data(self) -> None:
        """Загружает данные из хранилища"""
        try:
            self.storage.load(self.manager)
            print("Данные успешно загружены.")
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def save_data(self) -> None:
        """Сохраняет данные в хранилище."""
        try:
            self.storage.save(self.manager)
            print("Данные успешно сохранены")
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")

    def display_menu(self) -> None:
        """Отображает основное меню для взаимодействия с приложением."""
        print("\033[1;37m\n▐░░░░░░░ МЕНЮ ░░░░░░░░▌\033[0m")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Изменить задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Поиск задачи по ключевому слову")
        print("6. Удалить задачу")
        print("0. Выйти")

    def add_task(self):
        """Добавление новой задачи"""
        try:
            title = input("Введите заголовок задачи: ").strip()
            if not title:
                raise ValueError("Поле не может быть пустым")

            description = input("Введите описание задачи: ").strip()
            if not description:
                raise ValueError("Поле не может быть пустым")

            category = input("Введите категорию задачи: ").strip()
            if not category:
                raise ValueError("Поле не может быть пустым")

            due_date = input("Введите срок выполнения (ГГГГ-ММ-ДД): ").strip()
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Некорректный формат даты. Используйте формат ГГГГ-ММ-ДД.")

            valid_priority = {"низкий", "средний", "высокий"}
            priority = input(f"Введите приоритет задачи ({', '.join(valid_priority)}): ").strip()
            if not priority or priority not in valid_priority:
                raise ValueError(f"Допустимые значения для поля: {', '.join(valid_priority)}")

            self.manager.add_task(title, description, category, due_date, priority)
            print(f"Задача '{title}' добавлена.")
            self.save_data()
        except ValueError as e:
            print(f"Ошибка: {e}")

    def display_tasks(self):
        """Показать все задачи"""
        try:
            tasks = self.manager.display_tasks()
            if tasks:
                print("Список задач: ")
                print(f"{'ID':<9} | {'TITLE':<20} | {'DESCRIPTION':<20} | {'CATEGORY':<20} | {'DUE_DATE':<20} | {'PRIORITY':<20} | {'STATUS':<20}")
                print(f"{'-' * 140}")
                for task in tasks:
                    print(task)
            else:
                print("Список задач пуст. Чтобы добавить задачу, выберите пункт 2")
        except Exception as e:
            print(f"Ошибка: {e}")

    def edit_task(self):
        """Изменяет значение указанного поля задачи"""
        try:
            valid_fields = {"title", "description", "category", "due_date", "priority", "status"}
            task_id = int(input("Введите ID задачи, которую хотите изменить: ").strip())

            field = input(f"Введите поле, которое хотите изменить ({', ' .join(valid_fields)}): ").strip()
            if field not in valid_fields:
                raise ValueError(f"Поле '{field}' недопустимо. Доступные поля: {', '.join(valid_fields)}")

            value = input(f"Введите новое значение для поля '{field}': ").strip()
            if field == "due_date":
                try:
                    datetime.strptime(value, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Некорректный формат даты. Используйте формат ГГГГ-ММ-ДД.")

            self.manager.edit_task(task_id, field, value)
            self.save_data()
        except ValueError as e:
            print(f"Ошибка: {e}")

    def complete_task(self):
        """Отмечает задачу как выполненную"""
        try:
            task_id = int(input("Введите ID задачи: ").strip())
            if not isinstance(task_id, int) or not task_id:
                raise ValueError('ID задачи должен быть числом.')
            self.manager.complete_task(task_id)
            print(f"Задача с ID {task_id} отмечена как выполненная.")
            self.save_data()
        except Exception as e:
            print(f"Ошибкка: {e}")

    def search_tasks(self) -> None:
        """Задачи по ключевому слову"""
        try:
            keyword = input("Введите ключевое слово для поиска (ключевое слово/категория/статус): ").strip()
            if not keyword:
                raise ValueError("Ключевое слово для поиска не может быть пустым.")
            results = self.manager.search_tasks(keyword)
            if results:
                print(f"Найдено задач: {len(results)}")
                print(f"{'ID':<9} | {'TITLE':<20} | {'DESCRIPTION':<20} | {'CATEGORY':<20} | {'DUE_DATE':<20} | {'PRIORITY':<20} | {'STATUS':<20}")
                print(f"{'-' * 140}")
                for task in results:
                    print(task)
            else:
                print("Задачи не найдены.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def delete_task(self):
        """Удаляет задачу по ID."""
        print("Удаление задачи:")
        try:
            task_id = int(input("Введите ID задачи для удаления: ").strip())
            if not task_id:
                raise ValueError("ID задачи должен быть числом.")
            self.manager.delete_task(task_id)
            print(f"Задача с ID {task_id} удалена.")
            self.save_data()
        except TaskNotFoundError as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def exit_program(self) -> None:
        """Сохраняет данные и завершает программу."""
        self.save_data()
        print("Выход из программы.")
        exit(0)

    def run(self) -> None:
        """Запускает главное меню."""
        while True:
            self.display_menu()
            choice = input("\nВыберите действие: ").strip()
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("Неверный пункт меню. Попробуйте снова.")

