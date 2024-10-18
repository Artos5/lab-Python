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
