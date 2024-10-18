import math

def product (a_, b_):

    if(a_ >= 15): 
     z = math.sin(2*a_) + math.cos(2*b_)
    else:
     if(a>=0): # а повинно бути >= 0
      z = math.sqrt(a+b**2)
     else:
      z=-100; # обробка помилки

    return z

a = int(input("Введіть a (a не може бути менше 0): "))
while(a < 0):
 a = int(input("Помилка! Введіть a >= 0 (a не може бути менше 0): "))
b = int(input("Введіть b: "))

print("Результат = ", product (a, b))