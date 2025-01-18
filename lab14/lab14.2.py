
import matplotlib.pyplot as plt
import pandas as pd

# Завантажимо дані
ukraine_data = {
    'year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'value': [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 0]
}

us_data = {
    'year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'value': [5000, 4800, 4600, 4400, 4200, 4000, 3800, 3600, 3400, 3200, 3000, 2800, 2600, 2400, 2200, 2000, 1800, 1600, 1400, 1200, 1000]
}

df_ukraine = pd.DataFrame(ukraine_data)
df_us = pd.DataFrame(us_data)

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.plot(df_ukraine['year'], df_ukraine['value'], label='Україна')
plt.plot(df_us['year'], df_us['value'], label='США')
plt.xlabel('Рік')
plt.ylabel('Кількість дітей, які не ходять до школи')
plt.title('Динаміка кількості дітей, які не ходять до школи, в Україні та США')
plt.legend()
plt.show()

# Побудова стовпчастих діаграм
country = input("Введіть назву країни (Україна/США): ")
if country == 'Україна':
    plt.bar(df_ukraine['year'], df_ukraine['value'])
    plt.xlabel('Рік')
    plt.ylabel('Кількість дітей, які не ходять до школи')
    plt.title('Кількість дітей, які не ходять до школи, в Україні')
elif country == 'США':
    plt.bar(df_us['year'], df_us['value'])
    plt.xlabel('Рік')
    plt.ylabel('Кількість дітей, які не ходять до школи')
    plt.title('Кількість дітей, які не ходять до школи, в США')
else:
    print("Невірна назва!")
plt.show()
