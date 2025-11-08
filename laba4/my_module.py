import math
import random

# Математические функции
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def fibonacci(n):
    """Числа Фибоначчи до n-го элемента"""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

def is_prime(num):
    """Проверяет, является ли число простым"""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Работа со строками
def greet(name):
    return f"Привет, {name}!"

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    """Считает количество гласных в строке"""
    vowels = "аеёиоуыэюяaeiou"
    return sum(1 for char in text.lower() if char in vowels)

# Игровая функция
def guess_number(min_num=1, max_num=100):
    """Игра 'Угадай число'"""
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"Я загадал число от {min_num} до {max_num}. Попробуй угадать!")
    
    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1
            
            if guess < secret_number:
                print("Слишком маленькое!")
            elif guess > secret_number:
                print("Слишком большое!")
            else:
                print(f"Поздравляю! Ты угадал за {attempts} попыток!")
                break
        except ValueError:
            print("Пожалуйста, введите число!")