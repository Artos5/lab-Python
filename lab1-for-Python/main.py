from file_math import product

a = int(input("Введіть a (a не може бути менше 0): "))
while(a < 0):
 a = int(input("Помилка! Введіть a >= 0 (a не може бути менше 0): "))
b = int(input("Введіть b: "))

print("Результат = ", product (a, b))