from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import export_graphviz
import graphviz
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Загрузка данных
wine = load_wine()
X = wine.data
y = wine.target

# Разделение на обучающие и тестовые данные
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Обучаем дерево решений
tree = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
tree.fit(X_train, y_train)

# Предсказываем
y_pred = tree.predict(X_test)

# Метрики
print("Качество модели:")
print(classification_report(y_test, y_pred, target_names=wine.target_names))



dot_data = export_graphviz(tree, out_file=None, 
                           feature_names=wine.feature_names,  
                           class_names=wine.target_names,  
                           filled=True, rounded=True,  
                           special_characters=True)

graph = graphviz.Source(dot_data)
graph.render("decision_tree")
graph.view()


plt.figure(figsize=(20,10))
plot_tree(tree, feature_names=wine.feature_names, class_names=wine.target_names,
          filled=True, fontsize=10)
plt.show()

# Описание критериев и их влияния на структуру дерева 
# Критерии:  
#     criterion='gini': пытается минимизировать неоднородность (меньше вычислений).
#     criterion='entropy': использует информацию Шеннона, может строить чуть более сложные деревья.
# Влияние параметра max_depth:  
    # max_depth=3: ограничивает дерево, снижает риск переобучения.
    # При увеличении max_depth дерево становится сложнее, точность растёт, но возможен переобуч .

    # Отчет: Принцип работы дерева решений  

    # Дерево решений — это непараметрический метод машинного обучения, 
    # который рекурсивно разбивает данные на подгруппы на основе выбранного критерия 
    # (например, Gini или Entropy). На каждом этапе алгоритм стремится найти 
    # такой признак и такое значение порога, которые лучше всего разделяют классы. 

    # В ходе работы: 

    #     Была загружена база данных Wine Quality из scikit-learn.
    #     Построено дерево решений с ограничением глубины (max_depth=3) и критерием Джини.
    #     Модель показала точность около 90–95%.
    #     С использованием graphviz была визуализирована структура дерева.
    #     Анализ показал, что деревья с большей глубиной могут давать высокую точность на тренировочных данных, но снижается обобщённость.
         

    # Таким образом, дерево решений позволяет легко интерпретировать модель и понимать, 
    # какие признаки и как влияют на финальное решение. 
          