import matplotlib.pyplot as plt

# Дані про відсоток дівчат та хлопців
labels = ['Дівчата', 'Хлопці']
sizes = [55, 45]  # Значення
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # Відокремлення першого сегменту

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Розподіл учнів 7 класу за статтю')
plt.axis('equal')  
plt.show()

