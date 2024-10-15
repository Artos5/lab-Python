n = 4
for i in range(0, n + 1):
 num = 5
 for j in range(0, n+1, 1):
   if j > i:
    print(" ", end = " ")
   else:
    print(num, end = " ")
    num -=1
 print("")

