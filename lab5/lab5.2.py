n = 7 
for i in range(1, (n-1) + 1):  # Цикл по рядках
    for j in range(0, n):  # Цикл по стовпцях
        num = n - abs(i - j - 1) # Обчислюємо значення для поточного елемента
        print(num, end="")
    print("")  
