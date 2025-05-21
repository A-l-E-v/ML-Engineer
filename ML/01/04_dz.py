# Проект: Прогнозирование стоимости подержанных автомобилей

# 1. Формулировка задачи регрессии
# Цель: Предсказать цену подержанного автомобиля на основе его технических характеристик, параметров двигателя и категориальных свойств (марка, тип кузова, вид топлива и т.д.).
# Обоснование:
#     Цена автомобиля зависит от множества факторов, как числовых (мощность двигателя, расход топлива), так и категориальных (марка, тип привода).
#     Задача соответствует регрессии, так как целевая переменная (price) является числовой.

# 2. Признаки и источники данных
# Признаки (на основе описания данных):
#     Числовые:
#         wheelbase (колесная база),
#         carlength (длина),
#         enginesize (объем двигателя),
#         horsepower (лошадиные силы),
#         boreratio (степень сжатия),
#         citympg (расход топлива в городе).
#     Категориальные:
#         CarName (марка),
#         fueltype (тип топлива),
#         drivewheel (привод),
#         carbody (тип кузова),
#         enginetype (тип двигателя).

# Источник данных: Датасет Car Price Prediction с Kaggle. Содержит 26 признаков и 205 наблюдений.

# https://www.kaggle.com/datasets/hellbuoy/car-price-prediction

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# Загрузка данных
data = pd.read_csv('CarPrice_Assignment.csv')

# Удаление некритичных признаков
data = data.drop(['car_ID', 'symboling'], axis=1)

# Определение признаков
numeric_features = ['wheelbase', 'carlength', 'enginesize', 'horsepower', 'boreratio', 'citympg']
categorical_features = ['CarName', 'fueltype', 'drivewheel', 'carbody', 'enginetype']

# Пайплайн предобработки
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

X = preprocessor.fit_transform(data.drop('price', axis=1))
y = data['price']


# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение моделей
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
forest_model.fit(X_train, y_train)

# Функция оценки
def evaluate_model(model, X_test, y_test):
    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    return mae, r2

# Результаты
linear_mae, linear_r2 = evaluate_model(linear_model, X_test, y_test)
forest_mae, forest_r2 = evaluate_model(forest_model, X_test, y_test)
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
forest_model.fit(X_train, y_train)

# Функция оценки
def evaluate_model(model, X_test, y_test):
    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    return mae, r2

# Результаты
linear_mae, linear_r2 = evaluate_model(linear_model, X_test, y_test)
forest_mae, forest_r2 = evaluate_model(forest_model, X_test, y_test)

print(f"Линейная регрессия:")
print(f"MAE: {linear_mae:.2f}")
print(f"R² Score: {linear_r2:.2f}")

print("\nСлучайный лес:")
print(f"MAE: {forest_mae:.2f}")
print(f"R² Score: {forest_r2:.2f}")

# =============================================
# Линейная регрессия:
# MAE: 3841.24
# R² Score: 0.65

# Случайный лес:
# MAE: 1429.84
# R² Score: 0.95
# ===============================================

# Анализ результатов:  

#     Линейная регрессия:  Хотя модель проста и быстра, она может не улавливать сложные взаимосвязи между признаками и целевой переменной. Это приводит к относительно низкому R² Score и высокому MAE.
#     Случайный лес:  Модель показывает лучшие результаты по сравнению с линейной регрессией благодаря своей способности улавливать нелинейные зависимости и взаимодействия между признаками. Однако случайный лес может быть более чувствителен к выбросам и требует больше ресурсов для обучения.
     
# Заключение:  

# На основе полученных результатов можно сделать вывод, что случайный лес  лучше предсказывает цены автомобилей, чем линейная регрессия. Тем не менее, для дальнейшего улучшения модели можно рассмотреть следующие шаги: 

#     Обработка выбросов:  Идентифицировать и корректно обработать аномальные значения в данных.
#     Feature Engineering:  Создать новые признаки или преобразовать существующие для улучшения модели.
#     Гиперпараметры:  Подобрать оптимальные гиперпараметры для случайного леса с использованием Grid Search или Randomized Search.
#     Другие модели:  Проверить другие алгоритмы, такие как Gradient Boosting или XGBoost, которые могут показать еще лучшие результаты.
     