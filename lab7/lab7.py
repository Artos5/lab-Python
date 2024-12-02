# Дані про оцінки учнів з 12 предметів
students = {
    'Биченок': [80, 75, 90, 85, 88, 92, 78, 85, 84, 90, 91, 85],
    'Коноз': [60, 65, 70, 72, 68, 75, 74, 70, 75, 80, 85, 78],
    'Кучеренко': [95, 90, 92, 88, 91, 89, 87, 93, 90, 92, 94, 90],
    'Кучерявий': [70, 75, 72, 68, 74, 70, 73, 75, 76, 72, 74, 73],
    'Левченко': [85, 80, 78, 82, 84, 87, 88, 85, 89, 83, 85, 84],
    'Паламар': [55, 60, 58, 62, 98, 63, 97, 61, 70, 67, 62, 60],
    'Попова': [90, 60, 58, 90, 59, 63, 66, 61, 66, 67, 76, 90],
    'Рожановський': [58, 60, 55, 62, 69, 63, 65, 61, 64, 88, 76, 73],
    'Снітко': [65, 61, 58, 65, 59, 63, 65, 78, 64, 81, 71, 60],
    'Угрімов': [96, 70, 90, 62, 90, 70, 65, 75, 90, 67, 97, 93],
}

# виведення на екран всіх значень словника
def print_all_students(students):
    for name, grades in students.items():
        print(f"{name}: {grades}")

# додавання нового запису до словника
def add_student(students, name, grades):
    students[name] = grades

# видалення запису зі словника
def remove_student(students, name):
    try:
        del students[name]
    except KeyError:
        print(f"Студента з іменем {name} не знайдено.")

# перегляд вмісту словника за відсортованими ключами
def print_sorted_students(students):
    for name in sorted(students.keys()):
        print(f"{name}: {students[name]}")

# розрахунк середньої оцінки
def calculate_average(grades):
    return sum(grades) / len(grades)

# вирішення завдання
def calculate_averages_and_print_above_class_average(students):
    student_averages = {name: calculate_average(grades) for name, grades in students.items()}
    class_average = calculate_average(list(student_averages.values()))
    above_class_average = {name for name, avg in student_averages.items() if avg > class_average}

    print("Середні оцінки учнів:")
    for name, avg in student_averages.items():
        print(f"{name}: {avg:.2f}")

    print(f"\nСередня оцінка всього класу: {class_average:.2f}")
    print("\nУчні з середньою оцінкою вище середньої в класі:")
    for name in above_class_average:
        print(name)

# діалог по роботі зі словником
def main():
    while True:
        print("\nОберіть дію:")
        print("1. Вивести всі значення словника")
        print("2. Додати нового студента")
        print("3. Видалити студента")
        print("4. Переглянути словник за відсортованими ключами")
        print("5. Розрахувати середні оцінки і вивести учнів з середньою оцінкою вище середньої в класі")
        print("6. Вийти")

        choice = input("Введіть дію: ")

        if choice == '1':
            print_all_students(students)
        elif choice == '2':
            name = input("Введіть прізвище студента: ")
            grades = list(map(int, input("Введіть оцінки студента через пробіл: ").split()))
            add_student(students, name, grades)
        elif choice == '3':
            name = input("Введіть прізвище студента для видалення: ")
            remove_student(students, name)
        elif choice == '4':
            print_sorted_students(students)
        elif choice == '5':
            calculate_averages_and_print_above_class_average(students)
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

