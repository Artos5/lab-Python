
import json

# Дані про оцінки учнів у форматі JSON (початковий вміст)
data = {
    "students": [
        {"name": "Биченок", "grades": [81, 85, 90, 75, 88]},
        {"name": "Коноз", "grades": [60, 70, 65, 75, 68]},
        {"name": "Кучеренко", "grades": [95, 92, 88, 91, 89]},
        {"name": "Кучерявий", "grades": [78, 72, 68, 74, 73]},
        {"name": "Левченко", "grades": [85, 78, 82, 84, 87]},
        {"name": "Паламар", "grades": [67, 65, 60, 63, 79]},
        {"name": "Попова", "grades": [78, 80, 79, 81, 83]},
        {"name": "Рожановський", "grades": [90, 85, 87, 89, 91]},
        {"name": "Снітко", "grades": [65, 68, 72, 70, 74]},
        {"name": "Угрімов", "grades": [93, 86, 95, 91, 94]}
    ]
}

# Запис початкових даних у файл
with open('students.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Функція для виведення вмісту JSON файлу на екран
def print_json_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        print(json.dumps(data, ensure_ascii=False, indent=4))

# Функція для додавання нового запису у JSON файл
def add_student(filename, name, grades):
    with open(filename, 'r') as f:
        data = json.load(f)
    data["students"].append({"name": name, "grades": grades})
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Функція для видалення запису з JSON файлу
def remove_student(filename, name):
    with open(filename, 'r') as f:
        data = json.load(f)
    data["students"] = [student for student in data["students"] if student["name"] != name]
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Функція для пошуку даних за одним із полів на вибір
def search_student(filename, field, value):
    with open(filename, 'r') as f:
        data = json.load(f)
    result = [student for student in data["students"] if student.get(field) == value]
    return result

# Функція для розрахунку середньої оцінки кожного учня і всього класу
def calculate_averages(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    def calculate_average(grades):
        return sum(grades) / len(grades)

    student_averages = {student["name"]: calculate_average(student["grades"]) for student in data["students"]}
    class_average = calculate_average(list(student_averages.values()))
    above_class_average = {name for name, avg in student_averages.items() if avg > class_average}

    result = {
        "student_averages": student_averages,
        "class_average": class_average,
        "above_class_average": list(above_class_average)
    }

    with open('averages.json', 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

# Діалоговий режим
def main():
    while True:
        print("\nОберіть дію:")
        print("1. Вивести вміст JSON файлу")
        print("2. Додати нового студента")
        print("3. Видалити студента")
        print("4. Пошук студента за ім'ям")
        print("5. Розрахувати середні оцінки і зберегти результат")
        print("6. Вийти")

        choice = input("Введіть номер дії: ")

        if choice == '1':
            print_json_file('students.json')
        elif choice == '2':
            name = input("Введіть прізвище студента: ")
            grades = list(map(int, input("Введіть оцінки студента через пробіл: ").split()))
            add_student('students.json', name, grades)
        elif choice == '3':
            name = input("Введіть прізвище студента для видалення: ")
            remove_student('students.json', name)
        elif choice == '4':
            name = input("Введіть прізвище студента для пошуку: ")
            result = search_student('students.json', 'name', name)
            if result:
                print("Знайдено студента:")
                print(json.dumps(result, ensure_ascii=False, indent=4))
            else:
                print("Студента не знайдено.")
        elif choice == '5':
            calculate_averages('students.json')
            print_json_file('averages.json')
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()