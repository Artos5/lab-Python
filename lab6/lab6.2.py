def process_list():
    # Введення списку з клавіатури
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()  # Розбиваємо рядок на список елементів
    new_list = lst[1::2]  # Вибираємо елементи

    # Виведення результатів
    print("Початковий список:", lst)
    print("Новий список (кожен другий елемент):", new_list)

# Виклик функції
process_list()
