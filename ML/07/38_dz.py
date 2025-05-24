import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris  # Используем встроенный набор данных
import matplotlib.pyplot as plt

# Загрузка данных
data = load_iris()
X = data.data
y = data.target

# Задание 1: Метод k-ближайших соседей при k=3
# Разбиение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Нормализация данных (важно для k-NN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_scaled = scaler.fit_transform(X)

# Обучение модели при k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Предсказание и оценка
y_pred = knn.predict(X_test_scaled)
accuracy_k3 = accuracy_score(y_test, y_pred)
print(f"Точность при k=3: {accuracy_k3:.2f}")

# Задание 2: Влияние числа соседей на качество классификации
# Перебор значений k
k_values = list(range(1, 11))
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

# Визуализация
plt.plot(k_values, accuracies, marker='o')
plt.title('Зависимость точности от значения k')
plt.xlabel('k')
plt.ylabel('Точность')
plt.grid(True)
plt.show()

# Задание 3: Кросс-валидация для выбора оптимального k
# Кросс-валидация
cv_scores = []
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_scaled, y, cv=kfold, scoring='accuracy')
    cv_scores.append(scores.mean())

# Поиск лучшего k
best_k = k_values[np.argmax(cv_scores)]
print(f"Лучшее значение k: {best_k} со средней точностью: {max(cv_scores):.2f}")

# График кросс-валидации
plt.plot(k_values, cv_scores, marker='o', color='orange')
plt.title('Кросс-валидация: Точность vs k')
plt.xlabel('k')
plt.ylabel('Средняя точность (5-Fold CV)')
plt.grid()
plt.show()

# Коэффициент силуэта (Silhouette Score)
from sklearn.metrics import silhouette_score

silhouette_scores = []

for k in range(2, 11):  # силуэт не определён для k=1
    knn = KNeighborsClassifier(n_neighbors=k)
    labels = knn.fit(X_train_scaled, y_train).predict(X_test_scaled)
    score = silhouette_score(X_test_scaled, labels)
    silhouette_scores.append(score)

# График силуэта
plt.plot(range(2, 11), silhouette_scores, marker='o', color='green')
plt.title('Коэффициент силуэта от k')
plt.xlabel('k')
plt.ylabel('Silhouette Score')
plt.grid()
plt.show()