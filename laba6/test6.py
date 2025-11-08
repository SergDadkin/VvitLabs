class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Приватный атрибут

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль успешно изменен")

    def check_password(self, password):
        return password == self.__password

    def display_info(self):
        print(f"Имя пользователя: {self.username}")
        print(f"Email: {self.email}")


print("Создание аккаунта")

username = input("Введите имя пользователя: ")
email = input("Введите email: ")
password = input("Введите пароль: ")


user = UserAccount(username, email, password)
print("\nАккаунт успешно создан!")
user.display_info()


print("Проверка пароля")
test_password = input("Введите пароль для проверки: ")
if user.check_password(test_password):
    print("Пароль верный!")
else:
    print("Неверный пароль!")

# смена пароля
print("Изменение пароля")
new_password = input("Введите новый пароль: ")
user.set_password(new_password)

# Проверяем пароль
print("Проверка нового пароля")
test_new_password = input("Введите новый пароль для проверки: ")
if user.check_password(test_new_password):
    print(" Новый пароль подтвержден!")
else:
    print(" Пароль не совпадает!")
    







class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Транспортное средство: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        return f"Автомобиль: {self.make} {self.model}, тип топлива: {self.fuel_type}"


print("транспорта")

print("Создание базового транспорта")
make_vehicle = input("Введите марку транспортного средства: ")
model_vehicle = input("Введите модель транспортного средства: ")
vehicle = Vehicle(make_vehicle, model_vehicle)

print("Создание автомобиля")
make_car = input("Введите марку автомобиля: ")
model_car = input("Введите модель автомобиля: ")
fuel_type = input("Введите тип топлива (бензин/дизель/электричество/гибрид): ")

car = Car(make_car, model_car, fuel_type)

print("Информация о созданных транспортных средствах")
print(vehicle.get_info())
print(car.get_info())

print("полиморфизм")
vehicles = [vehicle, car]

print("Создание доп автомобиля")
make_car2 = input("Введите марку второго автомобиля: ")
model_car2 = input("Введите модель второго автомобиля: ")
fuel_type2 = input("Введите тип топлива второго автомобиля: ")

car2 = Car(make_car2, model_car2, fuel_type2)
vehicles.append(car2)

print("\n=== Все транспортные средства ===")
for i, v in enumerate(vehicles, 1):
    print(f"{i}. {v.get_info()}")