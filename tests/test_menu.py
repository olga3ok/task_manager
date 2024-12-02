import pytest
from task_manager.task import Task


# Тесты для класса Menu
def test_add_task(menu, monkeypatch):
    """Тест добавления задачи"""
    menu.manager.tasks = []
    inputs = iter(["Test Task", "Description", "Work", "2024-12-31", "средний"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.add_task()
    tasks = menu.manager.tasks
    assert len(tasks) == 1
    task = tasks[0]
    assert task.title == "Test Task"
    assert task.description == "Description"
    assert task.category == "Work"


@pytest.mark.parametrize(
    "inputs, task_data, expected_output",
    [
        (["1"], {"task_id": 1, "title": "Task1", "description": "Description", "category": "Work", "due_date": "2024-12-22", "priority": "средний", "status": "не выполнена"},
         "Задача с ID 1 отмечена как выполненная."),
    ],
)
def test_complete_task(menu, manager, inputs, task_data, expected_output, monkeypatch, capsys):
    """Тест завершения задачи"""
    if task_data:
        menu.manager.tasks.append(Task(**task_data))
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    menu.complete_task()
    captured = capsys.readouterr()
    assert expected_output in captured.out


@pytest.mark.parametrize(
    "inputs, task_data, expected_output",
    [
        (["1"], {"task_id": 1, "title": "Task1", "description": "Description", "category": "Work", "due_date": "2024-12-22", "priority": "средний", "status": "не выполнена"},
         "Задача с ID 1 удалена."),
        (["999"], None, "Задача с ID 999 не найдена."),
    ]
)
def test_delete_task(menu, inputs, task_data, expected_output, monkeypatch, capsys):
    """Тест удаления задачи"""
    if task_data:
        menu.manager.tasks.append(Task(**task_data))
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    menu.delete_task()
    captured = capsys.readouterr()
    assert expected_output in captured.out


def test_display_tasks_empty(menu, capsys):
    """Тест вывода списка задач (список пуст)"""
    menu.manager.tasks = []
    menu.display_tasks()
    captured = capsys.readouterr()
    assert "Список задач пуст. Чтобы добавить задачу, выберите пункт 2" in captured.out


def test_display_tasks_with_data(menu, capsys):
    """Тест вывода списка задач (список содержит задачи)."""
    menu.manager.tasks.append(Task(task_id=1, title="Task1", description="description", category="Work", due_date="2024-12-31", priority="средний"))
    menu.manager.tasks.append(Task(task_id=2, title="Task2", description="description", category="Work", due_date="2024-12-31", priority="средний"))

    menu.display_tasks()
    captured = capsys.readouterr()
    assert "Список задач: " in captured.out
    assert f"{'ID':<9} | {'TITLE':<20} | {'DESCRIPTION':<20} | {'CATEGORY':<20} | {'DUE_DATE':<20} | {'PRIORITY':<20} | {'STATUS':<20}" in captured.out
    assert f"{'-' * 140}"
    assert f"[ID: {'1':<3}] | {'Task1':<20} | {'description':<20} | {'Work':<20} | {'2024-12-31':<20} | {'средний':<20} | {'не выполнена':<20}"
    assert f"[ID: {'1':<3}] | {'Task2':<20} | {'description':<20} | {'Work':<20} | {'2024-12-31':<20} | {'средний':<20} | {'не выполнена':<20}"


@pytest.mark.parametrize(
    "inputs, existing_task, expected_output",
    [
        (["1", "title", "Updated Title"], {"task_id": 1, "title": "Task1", "description": "Description", "category": "Work", "due_date": "2024-12-22", "priority": "средний", "status": "не выполнена"},
         "Значение поля title изменено на Updated Title"),
        (["999", "title", "Updated Title"], None, "Задача с ID 999 не найдена."),

    ]
)
def test_edit_task(menu, inputs, existing_task, expected_output, monkeypatch, capsys):
    """Тест редактирования задачи"""
    if existing_task:
        menu.manager.tasks.append(Task(**existing_task))
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    menu.edit_task()
    captured = capsys.readouterr()
    assert expected_output in captured.out


@pytest.mark.parametrize(
    "inputs, existing_task, expected_output",
    [
        (["Task"], {"task_id": 1, "title": "Task1", "description": "Description", "category": "Work", "due_date": "2024-12-22", "priority": "средний", "status": "не выполнена"},
         "Найдено задач: 1"),
        (["unknown"], None, "Задачи не найдены."),

    ]
)
def test_search_task(menu, inputs, existing_task, expected_output, monkeypatch, capsys):
    """Тест поиска задачи по ключевому слову"""
    menu.manager.tasks = []
    if existing_task:
        menu.manager.tasks.append(Task(**existing_task))
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    menu.search_tasks()
    captured = capsys.readouterr()
    assert expected_output in captured.out
