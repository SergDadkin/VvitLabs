class Employee:
    def __init__(self, name: str, id: int):
        self._name = name
        self._id = id

    def get_info(self) -> str:
        return f"ID: {self._id}, Имя: {self._name}"

    def __str__(self):
        return self.get_info()


class Manager(Employee):
    def __init__(self, name: str, id: int, department: str):
        super().__init__(name, id)
        self._department = department
        self._subordinates = []

    def manage_project(self) -> str:
        return f"Менеджер {self._name} управляет проектами в отделе {self._department}"

    def add_employee(self, employee: Employee):
        self._subordinates.append(employee)
        return f"Сотрудник {employee._name} добавлен в команду"

    def get_team_info(self) -> list:
        return [emp.get_info() for emp in self._subordinates]

    def get_team_details(self) -> str:
        if not self._subordinates:
            return "В команде нет сотрудников"
        team_info = "\n".join([f"  - {emp.get_info()}" for emp in self._subordinates])
        return f"Команда менеджера {self._name}:\n{team_info}"


class Technician(Employee):
    def __init__(self, name: str, id: int, specialization: str):
        super().__init__(name, id)
        self._specialization = specialization

    def perform_maintenance(self) -> str:
        return f"Техник {self._name} выполняет техническое обслуживание в области {self._specialization}"

    def get_info(self) -> str:
        return f"ID: {self._id}, Имя: {self._name}, Специализация: {self._specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name: str, id: int, department: str, specialization: str):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)

    def __str__(self):
        return (f"TechManager: {self.get_info()}, "
                f"Отдел: {self._department}, "
                f"Специализация: {self._specialization}")

    def get_info(self) -> str:
        return f"ID: {self._id}, Имя: {self._name}"


class EmployeeSystem:
    def __init__(self):
        self.employees = []
        self.managers = []

    def input_employee(self):
        """Ввод данных обычного сотрудника"""
        print("\n=== Добавление обычного сотрудника ===")
        name = input("Введите имя сотрудника: ")
        while True:
            try:
                emp_id = int(input("Введите ID сотрудника: "))
                break
            except ValueError:
                print("Ошибка! ID должен быть числом. Попробуйте снова.")
        
        employee = Employee(name, emp_id)
        self.employees.append(employee)
        print(f"Сотрудник {name} успешно добавлен!")
        return employee

    def input_manager(self):
        """Ввод данных менеджера"""
        print("\n=== Добавление менеджера ===")
        name = input("Введите имя менеджера: ")
        while True:
            try:
                emp_id = int(input("Введите ID менеджера: "))
                break
            except ValueError:
                print("Ошибка! ID должен быть числом. Попробуйте снова.")
        
        department = input("Введите отдел менеджера: ")
        manager = Manager(name, emp_id, department)
        self.employees.append(manager)
        self.managers.append(manager)
        print(f" Менеджер {name} успешно добавлен!")
        return manager

    def input_technician(self):
        """Ввод данных техника"""
        print("\n=== Добавление техника ===")
        name = input("Введите имя техника: ")
        while True:
            try:
                emp_id = int(input("Введите ID техника: "))
                break
            except ValueError:
                print("Ошибка! ID должен быть числом. Попробуйте снова.")
        
        specialization = input("Введите специализацию техника: ")
        technician = Technician(name, emp_id, specialization)
        self.employees.append(technician)
        print(f"Техник {name} успешно добавлен!")
        return technician

    def input_tech_manager(self):
        """Ввод данных TechManager"""
        print("\n=== Добавление TechManager ===")
        name = input("Введите имя TechManager: ")
        while True:
            try:
                emp_id = int(input("Введите ID TechManager: "))
                break
            except ValueError:
                print("Ошибка! ID должен быть числом. Попробуйте снова.")
        
        department = input("Введите отдел: ")
        specialization = input("Введите специализацию: ")
        tech_manager = TechManager(name, emp_id, department, specialization)
        self.employees.append(tech_manager)
        self.managers.append(tech_manager)
        print(f"TechManager {name} успешно добавлен!")
        return tech_manager

    def add_employee_to_manager(self):
        """Добавление сотрудника в команду менеджера"""
        if not self.managers:
            print("Нет доступных менеджеров!")
            return
        
        if not self.employees:
            print(" Нет доступных сотрудников!")
            return

        print("\n=== Выбор менеджера ===")
        for i, manager in enumerate(self.managers, 1):
            print(f"{i}. {manager._name} (ID: {manager._id})")
        
        try:
            mgr_choice = int(input("Выберите менеджера (номер): ")) - 1
            selected_manager = self.managers[mgr_choice]
        except (ValueError, IndexError):
            print("Неверный выбор!")
            return

        print("\n=== Выбор сотрудника для добавления в команду ===")
        available_employees = [emp for emp in self.employees if emp != selected_manager]
        for i, emp in enumerate(available_employees, 1):
            print(f"{i}. {emp.get_info()}")
        
        try:
            emp_choice = int(input("Выберите сотрудника (номер): ")) - 1
            selected_employee = available_employees[emp_choice]
        except (ValueError, IndexError):
            print(" Неверный выбор!")
            return

        result = selected_manager.add_employee(selected_employee)
        print(f" {result}")

    def show_all_employees(self):
        """Показать всех сотрудников"""
        print("\n=== Все сотрудники ===")
        if not self.employees:
            print(" Нет сотрудников в системе")
            return
        
        for i, employee in enumerate(self.employees, 1):
            print(f"{i}. {employee.get_info()}")

    def show_team_info(self):
        """Показать информацию о командах менеджеров"""
        if not self.managers:
            print(" Нет менеджеров в системе")
            return
        
        print("\n=== Информация о командах ===")
        for manager in self.managers:
            print(manager.get_team_details())
            print("-" * 30)

    def perform_actions(self):
        """Выполнение специальных действий"""
        if not self.employees:
            print(" Нет сотрудников в системе")
            return

        print("\n=== Выбор сотрудника для действий ===")
        for i, employee in enumerate(self.employees, 1):
            print(f"{i}. {employee.get_info()}")
        
        try:
            choice = int(input("Выберите сотрудника (номер): ")) - 1
            selected_employee = self.employees[choice]
        except (ValueError, IndexError):
            print(" Неверный выбор!")
            return

        print(f"\n=== Действия для {selected_employee._name} ===")
        
        # Полиморфизм
        
        if isinstance(selected_employee, Manager):
            print(f" {selected_employee.manage_project()}")
        
        if isinstance(selected_employee, Technician):
            print(f"🔧 {selected_employee.perform_maintenance()}")

    def show_menu(self):
        """Главное меню системы"""
        while True:
            print("\n" + "="*50)
            print("        СИСТЕМА УПРАВЛЕНИЯ СОТРУДНИКАМИ")
            print("="*50)
            print("1. Добавить обычного сотрудника")
            print("2. Добавить менеджера")
            print("3. Добавить техника")
            print("4. Добавить TechManager")
            print("5. Показать всех сотрудников")
            print("6. Добавить сотрудника в команду менеджера")
            print("7. Показать информацию о командах")
            print("8. Выполнить специальные действия")
            print("9. Демонстрация полиморфизма")
            print("0. Выход")
            print("-"*50)

            choice = input("Выберите действие: ")

            if choice == '1':
                self.input_employee()
            elif choice == '2':
                self.input_manager()
            elif choice == '3':
                self.input_technician()
            elif choice == '4':
                self.input_tech_manager()
            elif choice == '5':
                self.show_all_employees()
            elif choice == '6':
                self.add_employee_to_manager()
            elif choice == '7':
                self.show_team_info()
            elif choice == '8':
                self.perform_actions()
            elif choice == '9':
                self.demo_polymorphism()
            elif choice == '0':
                print("До свидания!")
                break
            else:
                print(" Неверный выбор! Попробуйте снова.")

    def demo_polymorphism(self):
        """Демонстрация полиморфизма"""
        if not self.employees:
            print("Нет сотрудников для демонстрации!")
            return
        
        print("\n=== Демонстрация полиморфизма ===")
        print("Все сотрудники используют метод get_info(), но реализация разная:")
        print("-" * 40)
        
        for employee in self.employees:
            print(f" {employee.get_info()}")


# Запуск системы
if __name__ == "__main__":
    system = EmployeeSystem()
    system.show_menu()
    