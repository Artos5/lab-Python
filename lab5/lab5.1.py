n = int(input("n = "))
s = 0
print(f"Enter {n} array elements:")

arr = [int(input()) for _ in range(n)]
for i in range(len(arr)):  # цикл по кількості елементів списку
 if(arr[i]>0):
  s+=arr[i]
print("Сума додатніх чисел: ", s)
