import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 1. Загрузка данных
df = pd.read_csv("CarPrice_Assignment.csv")

# 2. Предобработка данных
# Удаление ненужных столбцов
df = df.drop(columns=["car_ID", "CarName"], errors='ignore')

# Кодирование категориальных переменных
df = pd.get_dummies(df, drop_first=True)

# Разделение на признаки и целевую переменную
X = df.drop("price", axis=1)
y = df["price"]

# Нормализация признаков
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 3. Обучение модели на оригинальных признаках
lr_orig = LinearRegression()
lr_orig.fit(X_train, y_train)
y_pred_orig = lr_orig.predict(X_test)

# 4. Генерация полиномиальных признаков
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Нормализация полиномиальных признаков
X_poly_scaled = scaler.fit_transform(X_poly)

# Разделение на обучающую и тестовую выборки
X_poly_train, X_poly_test, y_poly_train, y_poly_test = train_test_split(
    X_poly_scaled, y, test_size=0.2, random_state=42
)

# Обучение модели на полиномиальных признаках
lr_poly = LinearRegression()
lr_poly.fit(X_poly_train, y_poly_train)
y_pred_poly = lr_poly.predict(X_poly_test)

# 5. Оценка качества обеих моделей
print("Метрики на оригинальных признаках:")
print(f"R²: {r2_score(y_test, y_pred_orig):.4f}")
print(f"MSE: {mean_squared_error(y_test, y_pred_orig):.2f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred_orig):.2f}")

print("\nМетрики на полиномиальных признаках:")
print(f"R²: {r2_score(y_poly_test, y_pred_poly):.4f}")
print(f"MSE: {mean_squared_error(y_poly_test, y_pred_poly):.2f}")
print(f"MAE: {mean_absolute_error(y_poly_test, y_pred_poly):.2f}")

# 6. Визуализация результатов
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred_orig, alpha=0.7, color='blue')
plt.plot([min(y), max(y)], [min(y), max(y)], 'r--')
plt.title("Оригинальные признаки")
plt.xlabel("Реальные значения")
plt.ylabel("Предсказанные значения")

plt.subplot(1, 2, 2)
plt.scatter(y_poly_test, y_pred_poly, alpha=0.7, color='green')
plt.plot([min(y), max(y)], [min(y), max(y)], 'r--')
plt.title("Полиномиальные признаки")
plt.xlabel("Реальные значения")
plt.ylabel("Предсказанные значения")

plt.tight_layout()
plt.show()

# Результаты работы программы:
# Метрики на оригинальных признаках:
# R²: 0.8926
# MSE: 8482008.48
# MAE: 2089.38

# Метрики на полиномиальных признаках:
# R²: -206.1656
# MSE: 16354487484.98
# MAE: 67006.75

# Выводы по результатам 
# 1. Полиномиальные признаки без регуляризации могут ухудшить качество модели  

#     При добавлении полиномиальных признаков число признаков значительно возрастает.
#     Линейная регрессия без регуляризации не может справиться с таким количеством мультиколлинеарных и избыточных признаков.
#     Модель сильно переобучается  на обучающей выборке и плохо работает на тестовой .
     

# 2. Оригинальные признаки уже содержат достаточную информацию  

#     Модель на исходных признаках показывает отличные метрики (R² = 0.89).
#     Это говорит о том, что данные уже хорошо линейно разделимы , и нет необходимости усложнять модель с помощью полиномиальных признаков без дополнительной регуляризации или понижения размерности.
     

# 3. Визуализация подтверждает это:  

#     На графике предсказаний оригинальной модели точки близки к диагонали.
#     У модели с полиномиальными признаками предсказания сильно отклоняются от реальных значений — видны большие выбросы и нестабильность.
     