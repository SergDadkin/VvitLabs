name = input('ваш ник: ')
def greet(name):
    print('ПРИВЕТ,', name)
greet(name)

    
num=int(input("Число="))
def square(num):
    print("Ответ =",num)
square(num)


import re
# x=input('Число1=')
# y=input('Число2=')
def max_of_two(s1,s2):
    n1=re.findall(r'-?\d+',x)
    n2=re.findall(r'-?\d+',y)
    s1=int(n1[0]) if n1 else 0
    s2=int(n2[0]) if n2 else 0
    if s1>s2:
        return(s1)
    elif s1<s2:
        return(s2)
    else:
        return(f'{s1}={s2}')
print("ввод чисел (ПРОБЕЛ-прирывание процесса)")
while True:
    x = input('Первое число: ')
    if x == ' ':
        break
    
    y = input('Второе число: ')
    if y == ' ':
        break
    
    result = max_of_two(x, y)
    print(f"Результат: {result}")




class Checker:
    def __init__(self):  #создание нового класса
        self.cache = {}  #пустой слов
    
    def is_prime(self, n):
        if not isinstance(n, int):  #True OR False
            return False
        
        if n in self.cache: # наличие в слов
            return self.cache[n]
        
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(n**0.5) + 1, 2):# перебор делителей
            if n % i == 0:
                self.cache[n] = False
                return False
        
        self.cache[n] = True
        return True

checker = Checker()

while True:
    try:
        user_input=input("Введите число для проверки (или 'выход' для завершения): ")
        
        if user_input.lower() in ['выход']:
            break
            
        number = int(user_input)
        result = checker.is_prime(number)
        status = "простое" if result else "составное"
        print(f"Число {number} является {status} числом")
        
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число")
    except KeyboardInterrupt:
        print("\nПрограмма завершена")
        break
    
    
    
  
def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")

name = input("Введите имя: ")
age_input = input("Введите возраст: ")

if age_input.strip() == "":
    describe_person(name)
else:
    try:
        age = int(age_input)
        describe_person(name, age)
    except ValueError:
        print("Введите число")
        describe_person(name)