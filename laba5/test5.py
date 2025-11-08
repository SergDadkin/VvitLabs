class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


def create_book():
    print("\n--- Создание новой книги ---")
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    
    while True:
        try:
            year = int(input("Введите год издания: "))
            break
        except ValueError:
            print("Ошибка! Введите корректный год (число).")
    
    return Book(title, author, year)


saved_books = []  # Список для хранения всех книг

# Создаем несколько книг
while True:
    new_book = create_book()
    saved_books.append(new_book)
    
    cont_adding = input("\nХотите добавить книги? (да/нет): ").lower()
    if cont_adding != 'да':
        break


print("ВСЕ СОХРАНЕННЫЕ КНИГИ:")
for i, book in enumerate(saved_books, 1):
    print(f"{i}. {book.get_info()}")




class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius


radius = float(input("Введите радиус круга: "))
circle = Circle(radius)

print(f"Радиус круга: {circle.get_radius()}")

answer = input("Изменить радиус? (да/нет): ")
if answer.lower() == 'да':
    new_radius = float(input("Введите новый радиус: "))
    circle.set_radius(new_radius)
    print(f"Новый радиус: {circle.get_radius()}")