def process_list():
    # Введення списку з клавіатури
    user_input = input("Введіть елементи списку через пробіл: ")
    lst = user_input.split()  # Розбиваємо рядок

    # Виведення результатів
    print("Введений список:", lst)
    print("Список у зворотному порядку:", lst[::-1]) # Вивід списку у зворотному порядку
    print("Кількість елементів у списку:", len(lst))

# Виклик функції
process_list()
