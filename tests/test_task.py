import pytest
from task_manager.task import Task


# Тесты для класса Task
def test_task_to_dict():
    """Тест преобразования данных объекта в словарь"""
    task = Task(1, "Test Task", "Description", "Work", "2024-12-31", "средний")
    task_dict = task.to_dict()
    assert task_dict == {
        "id": task.id,
        "title": "Test Task",
        "description": "Description",
        "category": "Work",
        "due_date": "2024-12-31",
        "priority": "средний",
        "status": "не выполнена",
    }


def test_task_from_dist():
    """Тест создания объекта из словаря данных"""
    data = {
        "id": 1,
        "title": "Test Task",
        "description": "Description",
        "category": "Work",
        "due_date": "2024-12-31",
        "priority": "средний",
        "status": "не выполнена",
    }
    task = Task.from_dict(data)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Description"
    assert task.category == "Work"
    assert task.due_date == "2024-12-31"
    assert task.priority == "средний"
    assert task.status == "не выполнена"
