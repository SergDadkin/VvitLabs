import math
import datetime

def calculate():
    num= float(input("Введите число: "))
    res= math.sqrt(num)
    print(f"Квадратный корень из {num} равен {res}")

def date():
    time_datetime = datetime.datetime.now()
    print(f"Текущая дата и время: {time_datetime.strftime('%d.%m.%Y %H:%M:%S')}")

calculate()
date()
#Основная программа не выполняется при импорте 
if __name__ == "__main__":
    calculate()
    date()


import my_module as mm
def main():
    # Сложение
    a = int(input("число для сложения: "))
    b = int(input("число для сложения: "))
    print(f"   Сумма {a} и {b}: {mm.add_numbers(a, b)}")
    
    # Умножение
    a = int(input("число для умножения: "))
    b = int(input(" число для умножения: "))
    print(f"   Произведение {a} и {b}: {mm.multiply_numbers(a, b)}")
    
    # Числа Фибоначчи
    n = int(input("Сколько чисел Фибоначчи показать? "))
    print(f"   Первые {n} чисел Фибоначчи: {mm.fibonacci(n)}")
    
    # Проверка на простое число
    num = int(input("Введите число для проверки на простоту: "))
    print(f"   Число {num} простое? {mm.is_prime(num)}\n")
    
    
    name = input("Введите ваше имя: ")
    print(f"   Приветствие: {mm.greet(name)}")
    
    text = input("Введите текст для анализа: ")
    print(f"   Перевернутый текст: {mm.reverse_string(text)}")
    print(f"   Количество гласных в тексте: {mm.count_vowels(text)}\n")
    
    # Игра
    print("3. ИГРА:")
    play_game = input("Хотите сыграть в 'Угадай число'? (да/нет): ").lower()
    if play_game == 'да':
        print()
        mm.guess_number()

if __name__ == "__main__":
    main()