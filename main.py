from task_manager.menu import Menu


def main() -> None:
    """Точка входа для запуска приложения."""
    print("Добро пожаловать в приложение \"Менеджер задач\"!")
    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()
