import pytest
from task_manager.storage import Storage, StorageError
from task_manager.task_manager import TaskManager


# Тесты для класса Storage
def test_save_and_load_empty(storage, manager):
    """Тест загрузки пустого списка"""
    new_storage = Storage(filename="test_storage.json")
    new_storage.load(manager)
    assert manager.tasks == []


def test_save_and_load_tasks(storage, manager):
    """Тест загрузки и сохранения списка задач"""
    manager.add_task("Task 1", "Description", "Work", "2024-12-31", "средний")
    manager.add_task("Task 2", "Description2", "Home", "2024-12-31", "высокий")

    storage.save(manager)
    loaded_manager = TaskManager()
    storage.load(loaded_manager)
    assert len(loaded_manager.tasks) == 2
    assert loaded_manager.tasks[0].id == 1
    assert loaded_manager.tasks[0].title == "Task 1"
    assert loaded_manager.tasks[0].status == "не выполнена"

    assert loaded_manager.tasks[1].description == "Description2"


def test_save_invalid_data(storage, manager):
    """Тест попытки сохранения некорректных данных"""
    manager.tasks = [{"invalid data"}]
    with pytest.raises(StorageError, match="Ошибка при сохранении данных."):
        storage.save(manager)





