import pytest
from task_manager.task_manager import TaskManager, TaskNotFoundError


# Тесты для класса TaskManager
def test_add_task(manager):
    """Тест добавления задачи"""
    task = manager.add_task("Test Task", "Description", "Work", "2024-12-31", "средний")
    assert len(manager.tasks) == 1
    assert manager.tasks[0] == task


def test_complete_task(manager):
    """Тест изменения статуса задачи на 'выполнена'"""
    task = manager.add_task("Test Task", "Description", "Work", "2024-12-31", "средний")
    manager.complete_task(task.id)
    assert task.status == "выполнена"


def test_complete_task_invalid_id(manager):
    """Тест изменения статуса задачи с несуществующим ID на 'выполнена'"""
    with pytest.raises(TaskNotFoundError):
        manager.complete_task(9999)


def test_delete_task(manager):
    """Тест удаления задачи из списка"""
    task = manager.add_task("Test Task", "Description", "Work", "2024-12-31", "средний")
    manager.delete_task(task.id)
    assert len(manager.tasks) == 0


def test_delete_task_invalid_id(manager):
    """Тест удаления задачи с несуществующим ID из списка"""
    with pytest.raises(TaskNotFoundError):
        manager.delete_task(9999)


def test_search_task(manager):
    """Тест поиска задачи по ключевому слову"""
    manager.add_task("Test Task", "Description", "Work", "2024-12-31", "средний")
    manager.add_task("Test Task2", "Description2", "Home", "2024-12-31", "высокий")
    result = manager.search_tasks("Test")
    assert len(result) == 2
    result = manager.search_tasks("Home")
    assert len(result) == 1
    result = manager.search_tasks("неизвестно")
    assert len(result) == 0


def test_display_tasks(manager):
    """Тест возвращения списка всех задач"""
    manager.add_task("Test Task 1", "Description", "Work", "2024-12-31", "средний")
    manager.add_task("Test Task 2", "Description2", "Home", "2024-12-31", "высокий")
    result = manager.display_tasks()
    assert len(result) == 2
    assert result[0].title == "Test Task 1"
    assert result[1].title == "Test Task 2"


def test_edit_task(manager):
    """Тест редактирования задачи"""
    task = manager.add_task("Test Task 1", "Description", "Work", "2024-12-31", "средний")
    edited_task = manager.edit_task(task.id, "title", "new_title")
    assert edited_task.title == "new_title"

    edited_task = manager.edit_task(task.id, "priority", "высокий")
    assert edited_task.priority == "высокий"

    # попытка отредактировать несуществующую задачу
    edited_task = manager.edit_task(999, "priority", "высокий")
    assert edited_task is None



