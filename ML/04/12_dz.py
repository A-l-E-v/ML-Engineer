import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. Загрузка данных
df = pd.read_csv("CarPrice_Assignment.csv")

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

# 2. Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 3. Оценка без кросс-валидации
r2_test = r2_score(y_test, y_pred)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred))

print("Метрики без кросс-валидации:")
print(f"R²: {r2_test:.4f}")
print(f"RMSE: {rmse_test:.2f}")

# 4. Кросс-валидация
cv_scores_r2 = cross_val_score(model, X_scaled, y, scoring='r2', cv=5)
cv_scores_rmse = -cross_val_score(model, X_scaled, y, scoring='neg_root_mean_squared_error', cv=5)

print("\nМетрики с кросс-валидацией (среднее по 5 фолдам):")
print(f"R²: {np.mean(cv_scores_r2):.4f}")
print(f"RMSE: {np.mean(cv_scores_rmse):.2f}")

# 5. Визуализация предсказаний
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y), max(y)], [min(y), max(y)], 'r--')
plt.title("Предсказания vs Реальные значения")
plt.xlabel("Реальные цены")
plt.ylabel("Предсказанные цены")
plt.grid(True)
plt.show()

# Результат:
# Метрики без кросс-валидации:
# R²: 0.8926
# RMSE: 2912.39

# Метрики с кросс-валидацией (среднее по 5 фолдам):
# R²: 0.3007
# RMSE: 5469.66

# Выводы:

# Кросс-валидация продемонстрировала, что модель плохо обобщает данные , несмотря на хорошие результаты на тестовой выборке

# Модель линейной регрессии показала высокое качество на тестовой выборке (R² = 0.89), но при использовании кросс-валидации её качество резко упало (R² = 0.30).  

# Это говорит о том, что модель переобучилась на обучающей выборке и плохо обобщает на новых данных.  

# Кросс-валидация позволила выявить эту проблему и дать более объективную оценку качества модели.  

# Таким образом, использование кросс-валидации важно для предотвращения переобучения и получения надёжной оценки качества модели.  

# Альтернативные методы оценки, такие как Bootstrap, LOO и Repeated K-Fold, также могут быть полезны в зависимости от задачи и объема данных.  
    

