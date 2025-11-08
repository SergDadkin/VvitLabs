def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")

def read_file_with_lines(filename):
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 0):
                print(f"Строка {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")

def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)



if __name__ == "__main__":

    read_file('1.txt')
    

    read_file_with_lines('1.txt')
    

    text_to_write = input("Введите текст для записи в файл: ")
    write_to_file('17.txt', text_to_write)
    

    text_to_append = input("Введите текст для дозаписи в файл: ")
    append_to_file('17.txt', text_to_append)
    

    read_file('17.txt')
    

    read_file('4.txt')