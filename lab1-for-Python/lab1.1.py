a = int(input ("Введіть а: "))

while (a < 1 or a > 100):

    a = int(input ("Невірне число a!\r\nВведіть ще раз а: "))

b = int(input ("Введіть b: "))

while (b < 1 or b > 100):

    b = int(input ("Невірне число b!\r\nВведіть ще раз b: "))

if a > b:

    r = a / b + 1

elif a == b:

    r = -2

else:

    r = (a - b) / a

print("Результат обчислення виразу: " , r)
