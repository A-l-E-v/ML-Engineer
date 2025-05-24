from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Задание 1: Определение важности признаков с помощью случайного леса  

# Загрузим пример данных
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Разделим данные на обучающие и тестовые
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создаем модель случайного леса
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Получаем важность признаков
importances = model.feature_importances_
feature_names = X.columns

# Создаем датафрейм для удобства отображения
feat_df = pd.DataFrame({'Признак': feature_names, 'Важность': importances})
feat_df = feat_df.sort_values(by='Важность', ascending=False)

# Визуализация
plt.figure(figsize=(10,6))
sns.barplot(x='Важность', y='Признак', data=feat_df, hue='Признак', dodge=False, palette='viridis', legend=False)
plt.title('Важность признаков в модели случайного леса')
plt.tight_layout()
plt.show()

# Признаки с наибольшей важностью — те, которые чаще всего использовались при разбиении узлов деревьев.
# В наборе Iris высокую важность может показать "petal width (cm)" , так как он хорошо разделяет классы.


# Задание 2: Кросс-валидация для оценки качества модели

from sklearn.model_selection import cross_val_score

# Используем тот же набор данных
from sklearn.ensemble import RandomForestClassifier

# Создаем модель
model = RandomForestClassifier(random_state=42)

# Проводим кросс-валидацию с 5 фолдами
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

# Выводим результаты
print("Точность на каждом фолде:", cv_scores)
print("Средняя точность (CV): {:.2f}%".format(cv_scores.mean() * 100))

# ВЫВОДЫ:
# Наиболее важные признаки  можно определить по графику — они оказывают наибольшее влияние на прогноз модели.
# Кросс-валидация  позволяет получить объективную оценку качества модели.
# Случайный лес — мощный инструмент, который не только достигает высокой точности, но и помогает понять, какие признаки наиболее информативны.
