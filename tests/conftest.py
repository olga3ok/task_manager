import pytest
from task_manager.task_manager import TaskManager
from task_manager.menu import Menu
from task_manager.storage import Storage


@pytest.fixture()
def manager():
    return TaskManager()


@pytest.fixture()
def menu():
    return Menu()


@pytest.fixture()
def storage():
    return Storage(filename="test_tasks.json")
