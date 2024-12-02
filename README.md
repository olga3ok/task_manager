# Task Manager Console App

## Описание проекта
Это консольное приложение для управления списком задач. Оно позволяет добавлять, редактировать, завершать, удалять и искать задачи ключевому слову, а также сохранять данные в json и загружать их.

___
- Python 3.8+
- JSON для хранения данных
- Pytest для тестирования
---

## Функционал
### Основные возможности
- **Добавление задачи** с указание заголовка, описания, категории, даты выполнения, приоритета и статуса.

- **Редактирование задачи**: возможность обновить любое поле существующей задачи

- **Поиск задачи** по категории, заголовку и другим параметрам

- **Завершение задачи**: изменение статуса задачи на "выполнена"

- **Удаление задачи** по уникальному идентификатору

- **Просмотр всех задач**

- **Сохранение и загрузка данных** в JSON-файл

- **Меню и навигация**: текстовое меню для выбора действия

- **Выход из приложения** автоматически сохраняет текущие данные

---

## Структура проекта:
### Основные компоненты:
- **`Task`**: Задача с полями `id`, `title`, `description`, `category`, `due_date`, `priority`, `status`
- **`TaskManager`**: Класс для управления списком задач. Методы добавления, удаления, поиска, изменения статуса, редактирования, отображения списка всех задач
- **`Storage`**: Сохранение и загрузка данных из файла
- **`Menu`**: Взаимодействие с пользователем через текстовый интерфейс

---

## Установка и запуск приложения
1. **Клонируйте репозиторий**:
   ```bash
   git clone git@github.com:olga3ok/task_manager.git
   cd task_manager

2. **Убедитесь, что у вас установлен Python версии 3.8 или выше**
3. **Запустите приложение**:
  ```bash
  python main.py
  ```
---

## Тестирование
Для тестирования используется pytest. Для запуска тестов:
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Выполните команду:
  ```bash
  python -m pytest tests  