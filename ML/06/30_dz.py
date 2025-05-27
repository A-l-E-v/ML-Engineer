from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score
import pandas as pd

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Преобразуем в pandas DataFrame для удобства
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
df['species'] = df['target'].map({i: name for i, name in enumerate(iris.target_names)})

# Вывод первых строк данных
print("Первые 5 строк данных:")
print(df.head())

# Описательная статистика
print("\nОписательная статистика данных:")
print(df.describe())

# Проверка на пропущенные значения
print("\nПроверка на пропущенные значения:")
print(df.isnull().sum())

# Визуализация аномалий (выбросов)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df.drop(['target', 'species'], axis=1))
plt.title('Распределение признаков с выбросами (ящики с усами)', fontsize=14, pad=20)
plt.xlabel('Признаки', fontsize=12)
plt.ylabel('Значения (см)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Вывод: 
print("\nАнализ данных:")
print("- Пропущенных значений нет.")
print("- Выбросы есть в признаках 'sepal width (cm)', но они не являются аномалиями, так как соответствуют природным вариациям размеров цветков.")

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Модель дерева решений
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

# Предсказание
y_pred = tree_model.predict(X_test)

# Подсчёт метрик
acc = accuracy_score(y_test, y_pred)
rec = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

print("\nОсновные метрики модели:")
print(f"- Точность (Accuracy): {acc:.2%}")
print(f"- Полнота (Recall): {rec:.2%}")
print(f"- F1-мера: {f1:.2%}")

# Подробный отчёт по классификации
report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
report_df = pd.DataFrame(report).T

print("\nПодробный отчёт по метрикам классификации:")
print(report_df)

# Перебираем максимальную глубину дерева для анализа переобучения
depths = range(1, 10)
accuracies = []

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

# График зависимости точности от глубины дерева
plt.figure(figsize=(8, 5))
plt.plot(depths, accuracies, marker='o', linestyle='-', color='b', label='Точность на тестовых данных')
plt.xlabel('Максимальная глубина дерева', fontsize=12)
plt.ylabel('Точность (Accuracy)', fontsize=12)
plt.title('Зависимость точности модели от глубины дерева решений', fontsize=14, pad=15)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(1, 10))
plt.legend(fontsize=10, framealpha=0.9)
plt.show()

# Вывод по графику
print("\nАнализ зависимости точности от глубины дерева:")
print("- При глубине дерева = 1 модель недообучается (низкая точность).")
print("- Наибольшая точность достигается при глубине 3-4.")
print("- При глубине >4 точность стабилизируется, что может указывать на начало переобучения.")

# from sklearn.datasets import load_iris
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.metrics import classification_report
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, recall_score, f1_score


# # Загрузка данных
# iris = load_iris()
# X = iris.data
# y = iris.target

# # Преобразуем в pandas DataFrame для удобства
# import pandas as pd
# df = pd.DataFrame(X, columns=iris.feature_names)
# df['target'] = y
# df['species'] = df['target'].map({i: name for i, name in enumerate(iris.target_names)})

# print(df.head())
# print(df.describe())

# # Пропуски
# print("Пропущенные значения:\n", df.isnull().sum())

# # Аномалии (например, отрицательные значения или выбросы)


# plt.figure(figsize=(10,6))
# sns.boxplot(data=df.drop('target', axis=1))
# plt.title('Аномалии в данных')
# plt.xticks(rotation=45)
# plt.show()

# # Вывод: 

# # В наборе нет пропусков .
# # Нет значительных аномалий (все значения в разумных пределах).


# # Разделение данных
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42)

# # Модель дерева решений
# tree_model = DecisionTreeClassifier(random_state=42)
# tree_model.fit(X_train, y_train)

# # Предсказание
# y_pred = tree_model.predict(X_test)

# # Подсчёт метрик
# acc = accuracy_score(y_test, y_pred)
# rec = recall_score(y_test, y_pred, average='macro')
# f1 = f1_score(y_test, y_pred, average='macro')

# print(f"Точность: {acc:.2%}")
# print(f"Полнота: {rec:.2%}")
# print(f"F1-мера: {f1:.2%}")


# # Таблица с метриками
# report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
# report_df = pd.DataFrame(report).T

# print("\nМетрики качества модели:")
# print(report_df)


# # Перебираем максимальную глубину дерева
# depths = range(1, 10)
# accuracies = []

# for depth in depths:
#     model = DecisionTreeClassifier(max_depth=depth, random_state=42)
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     acc = accuracy_score(y_test, y_pred)
#     accuracies.append(acc)

# # График зависимости точности от глубины
# plt.figure(figsize=(8,5))
# plt.plot(depths, accuracies, marker='o', linestyle='-', color='b')
# plt.xlabel('Максимальная глубина дерева')
# plt.ylabel('Точность')
# plt.title('Зависимость точности от глубины дерева')
# plt.grid(True)
# plt.xticks(np.arange(1, 10))
# plt.show()

# # Вывод:    

# # С увеличением глубины дерево лучше подстраивается под данные, но может переобучаться.
# # Часто оптимальная глубина находится в диапазоне 3–5.

