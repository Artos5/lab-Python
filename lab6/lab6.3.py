def find_lett():
    # Введення тексту
    txt = input("Введіть текст з латинських літер: ").lower()  # Перетворюємо в нижній регістр 

    # Фільтруємо лише літери
    letters = [char for char in txt if char.isalpha()]

    # Створюємо словник
    frequency = {}
    for letter in letters:
        frequency[letter] = frequency.get(letter, 0) + 1

    # Вибираємо літери, які зустрічаються один раз
    unique_lett = [letter for letter, count in frequency.items() if count == 1]

    # Виведення результату
    print("Літери, які входять в текст один раз:", " ".join(unique_lett))

# Виклик функції
find_lett()

