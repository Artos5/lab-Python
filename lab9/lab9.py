import os

def create_file_TF17_1(filename):
    with open(filename, 'w') as f:
        f.write("Привіт!Це моя програма на Пітон! Тут є і букви і цифри: 12345\n")
        f.write("Мені подобається мова Python!\n")
        f.write("1234567890\n")

def process_files(input_file, temp_file, output_file):
    digits = []
    others = []

    with open(input_file, 'r') as f:
        for line in f:
            for char in line:
                if char.isdigit():
                    digits.append(char)
                elif char.isalpha() or char in [' ', '.', '!', '\n']:
                    others.append(char)

    with open(temp_file, 'w') as tf:
        tf.write(''.join(digits))
        tf.write(''.join(others))

    with open(temp_file, 'r') as tf, open(output_file, 'w') as of:
        data = tf.read()
        for i in range(0, len(data), 10):
            of.write(data[i:i+10] + '\n')

def print_file_content(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')

# Створення файлу TF17_1
create_file_TF17_1('TF17_1.txt')

# Обробка файлів та запис у TF17_2
process_files('TF17_1.txt', 'TF17_3.txt', 'TF17_2.txt')

# Читання та друк вмісту файлу TF17_2
print("Вміст файла TF17_2:")
print_file_content('TF17_2.txt')

# Видалення допоміжного файлу
os.remove('TF17_3.txt')