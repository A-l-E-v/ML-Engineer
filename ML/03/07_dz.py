import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Данные
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([50, 55, 65, 70, 75])

# Линейная регрессия (степень 1)
coeff_linear = np.polyfit(X.flatten(), y, deg=1)
poly_linear = np.poly1d(coeff_linear)

# Полиномиальная регрессия (степень 4)
coeff_poly = np.polyfit(X.flatten(), y, deg=4)
poly_higher = np.poly1d(coeff_poly)

# Предсказания на обучающих данных
y_pred_linear = poly_linear(X)
y_pred_poly = poly_higher(X)

# MSE на обучающих данных
mse_linear = mean_squared_error(y, y_pred_linear)
mse_poly = mean_squared_error(y, y_pred_poly)

# Вывод информации
print("==============================================")
print("        Анализ линейной и полиномиальной     ")
print("                  регрессий                    ")
print("==============================================\n")

print("Уравнения моделей:")
print(f"Линейная регрессия: {poly_linear}")
print(f"Полиномиальная регрессия (4-й степени): {poly_higher}\n")

print("Результаты на обучающей выборке:")
print(f"MSE линейной модели: {mse_linear:.4f}")
print(f"MSE полиномиальной модели: {mse_poly:.4f}\n")

print("Таблица предсказаний и ошибок:")
print("{:<8}{:<8}{:<15}{:<15}{:<10}{:<10}".format("X", "Y", "Y_lin", "Y_poly", "Ошибка лин", "Ошибка пол"))
for i in range(len(X)):
    x_val = X[i][0]
    y_val = y[i]
    y_lin_val = y_pred_linear[i].item()  # Извлечение как float
    y_poly_val = y_pred_poly[i].item()   # Извлечение как float
    error_lin = round(y_val - y_lin_val, 2)
    error_poly = round(y_val - y_poly_val, 2)
    print(f"{x_val:<8}{y_val:<8}{y_lin_val:<15.2f}{y_poly_val:<15.2f}{error_lin:<10.2f}{error_poly:<10.2f}")

# График
X_plot = np.linspace(0.5, 5.5, 100).reshape(-1, 1)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='black', label='Исходные данные')
plt.plot(X_plot, poly_linear(X_plot), color='blue', linestyle='--', label='Линейная модель')
plt.plot(X_plot, poly_higher(X_plot), color='red', label='Полиномиальная модель (deg=4)')
plt.title('Сравнение линейной и полиномиальной регрессии')
plt.xlabel('Часы подготовки')
plt.ylabel('Оценка')
plt.legend()
plt.grid(True)
plt.show()

# Вывод анализа
print("\n\n==============================================")
print("                 Анализ результатов           ")
print("==============================================\n")

print("Вывод:")
print("1. Обе модели идеально подогнались под обучающие данные.")
print("   Это видно по тому, что полиномиальная модель проходит точно через каждую точку.\n")
print("2. Однако это является признаком ПЕРЕОБУЧЕНИЯ:")
print("   - Модель слишком сложная (высокая степень многочлена)")
print("   - Она запоминает данные, а не учится обобщать.\n")
print("3. Признаки переобучения:")
print("   - Резкие колебания графика вне диапазона X (экстраполяция нестабильна)")
print("   - Ошибка на новых данных будет выше, чем на обучении\n")
print("4. Линейная модель, напротив, проста и стабильна.")
print("   Она лучше подходит для этих данных, так как связь почти линейная.\n")
print("Заключение:")
print("Для малого набора данных (всего 5 точек) использование полиномиальной регрессии")
print("степени выше 2 может привести к переобучению. Лучше использовать линейную модель,")
print("или применять регуляризацию (например, Ridge или Lasso) в случае более сложных задач.")