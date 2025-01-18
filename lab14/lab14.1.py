import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def y(x):
    return -x ** np.cos(5 * x)

# Створення масиву значень x
x = np.linspace(0, 10, 1000)

# Обчислення значень y
y_values = y(x)

# Побудова графіка
plt.plot(x, y_values, linestyle='-', color='b', linewidth=2, label='Y(x) = -x^cos(5*x)')

# Додавання підписів до осей
plt.xlabel('x')
plt.ylabel('Y(x)')

# Додавання назви графіка
plt.title('Графік функції Y(x) = -x^cos(5*x)')

# Додавання легенди
plt.legend()

# Відображення графіка
plt.grid(True)
plt.show()

