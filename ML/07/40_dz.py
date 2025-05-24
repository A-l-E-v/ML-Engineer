import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, log_loss

# Задание 1. Реализация GMM и визуализация кластеров

# Создаем искусственный набор данных
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)

# Визуализируем истинные кластеры
plt.scatter(X[:, 0], X[:, 1], c=y_true, cmap='viridis', s=50)
plt.title("Истинные кластеры")
plt.show()

# Обучение GMM
gmm = GaussianMixture(n_components=4, random_state=42)
gmm_labels = gmm.fit_predict(X)

# Визуализация кластеров GMM
plt.scatter(X[:, 0], X[:, 1], c=gmm_labels, cmap='viridis', s=50)
plt.title("Кластеры (GMM)")
plt.show()

# То же для k-means
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', s=50)
plt.title("Кластеры (k-means)")
plt.show()

# Задание 2. Сравнение GMM и k-means через коэффициент силуэта
# Коэффициент силуэта для GMM
silhouette_gmm = silhouette_score(X, gmm_labels)

# Для k-means
silhouette_kmeans = silhouette_score(X, kmeans_labels)

print(f"Silhouette Score (GMM): {silhouette_gmm:.4f}")
print(f"Silhouette Score (k-means): {silhouette_kmeans:.4f}")

# Сравнение
if silhouette_gmm > silhouette_kmeans:
    print("Метод GMM показал лучшее разделение.")
else:
    print("Метод k-means показал лучшее разделение.")

# Задание 3. Оценка качества GMM через log-likelihood
# Log-likelihood от GMM
log_likelihood = gmm.score_samples(X).sum()
print(f"Log-likelihood (GMM): {log_likelihood:.2f}")

# K-means не предоставляет вероятностной интерпретации, но можно оценить инерцию (сумма квадратов расстояний до центроидов):
inertia = kmeans.inertia_
print(f"Inertia (k-means): {inertia:.2f}")

# ВЫВОДЫ:
# log_likelihood и inertia нельзя напрямую сравнивать, так как это разные метрики. Но обе говорят о качестве модели: чем выше log_likelihood, тем лучше; чем ниже inertia, тем лучше.
# GMM , если данные имеют сложную форму или важно учитывать вероятность принадлежности к кластеру.
# k-means , если важна скорость и простота, а данные приблизительно сферические.
